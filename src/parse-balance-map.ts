import { BigNumber, utils } from 'ethers';
import BalanceTree from './balance-tree';

const { isAddress, getAddress, parseUnits } = utils;

interface MerkleDistributorInfo {
  merkleRoot: string;
  tokenTotal: string;
  claims: {
    [account: string]: {
      index: number;
      amount: string;
      proof: string[];
      flags?: {
        [flag: string]: boolean;
      };
    };
  };
}

type OldFormat = { [account: string]: number | string; }
type NewFormat = { address: string; earnings: string; reasons: string; }

interface DataByAddress {
  [address: string]: {
    amount: BigNumber;
    flags?: {
      [flag: string]: boolean;
    };
  };
}

export function parseBalanceMap(balances: OldFormat | NewFormat[]): MerkleDistributorInfo {
  const balancesInNewFormat: NewFormat[] = Array.isArray(balances)
    ? balances
    : Object.keys(balances).map((account) => ({
        address: account,
        // Convert numeric values directly to the smallest unit as a BigNumber, properly handling decimals
        earnings: parseUnits(balances[account].toString(), 18).toString(),
        reasons: '',
      }));

  const dataByAddress: DataByAddress = balancesInNewFormat.reduce((memo, { address, earnings, reasons }) => {
    if (!isAddress(address)) {
      throw new Error(`Found invalid address: ${address}`);
    }
    const parsedAddress = getAddress(address);
    if (memo[parsedAddress]) {
      throw new Error(`Duplicate address: ${parsedAddress}`);
    }

    const amount = BigNumber.from(earnings);
    if (amount.lte(0)) {
      throw new Error(`Invalid amount for account: ${address}`);
    }

    const flags = {
      isSOCKS: reasons.includes('socks'),
      isLP: reasons.includes('lp'),
      isUser: reasons.includes('user'),
    };

    memo[parsedAddress] = { amount, flags: reasons ? flags : undefined };
    return memo;
  }, {} as DataByAddress);

  const sortedAddresses = Object.keys(dataByAddress).sort();

  const tree = new BalanceTree(
    sortedAddresses.map((address) => ({ account: address, amount: dataByAddress[address].amount }))
  );

  const claims = sortedAddresses.reduce((memo, address, index) => {
    const { amount, flags } = dataByAddress[address];
    memo[address] = {
      index,
      amount: amount.toHexString(),
      proof: tree.getProof(index, address, amount),
      flags,
    };
    return memo;
  }, {} as MerkleDistributorInfo["claims"]);

  const tokenTotal = sortedAddresses.reduce((memo, key) => memo.add(dataByAddress[key].amount), BigNumber.from(0));

  return {
    merkleRoot: tree.getHexRoot(),
    tokenTotal: tokenTotal.toHexString(),
    claims,
  };
}

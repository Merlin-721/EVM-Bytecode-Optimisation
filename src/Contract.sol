// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.17;

contract Contract {
    // Function to get the fibonacci number at index n
    function fibs(uint256 n) public pure returns (uint256) {
        uint256 root_5 = sqrt(5);

        return (((1 + root_5) / 2)**n - ((1 - root_5) / 2)**n) / root_5;
    }

    function sqrt(uint256 y) internal pure returns (uint256 z) {
        if (y > 3) {
            z = y;
            uint256 x = y / 2 + 1;
            while (x < z) {
                z = x;
                x = (y / x + x) / 2;
            }
        } else if (y != 0) {
            z = 1;
        }
    }
}

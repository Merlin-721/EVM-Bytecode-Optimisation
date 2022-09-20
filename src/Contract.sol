// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.10;

contract Contract {
    // Function to get the fibonacci number at index n
    function fibs(uint256 n) external pure returns (uint256 b) {
        if (n == 0) {
            return 0;
        }
        uint256 a = 1;
        b = 1;
        for (uint256 i = 2; i < n; i++) {
            uint256 c = a + b;
            a = b;
            b = c;
        }
        return b;
    }

    function fibs_short(uint256) external pure returns (uint256 b) {
        uint256 a = 0;
        b = 1;
        for (uint256 i = 1; i < n; i++) {
            uint256 c = a + b;
            a = b;
            b = c;
        }
        return b;
    }

    }
}

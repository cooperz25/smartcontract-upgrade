pragma solidity >=0.8.0;

contract BoxV2 {
    uint256 number;
    uint256 number2;

    function setNumber(uint256 _value) public {
        number = _value;
    }

    function getNumber() public view returns (uint256) {
        return number;
    }

    function increase() public {
        number = number + 1;
    }
}

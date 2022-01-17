pragma solidity >=0.8.0;

contract Box {
    uint256 number;

    function setNumber(uint256 _value) public {
        number = _value;
    }

    function getNumber() public view returns (uint256) {
        return number;
    }
}

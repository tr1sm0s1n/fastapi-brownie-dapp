# @version ^0.3.6

admin: address
struct Certificate:
    name: String[16]
    course: String[40]
    grade: String[1]
    date: String[16]

event Issued:
    id: indexed(uint256)
    course: String[40]
    date: String[16]

Certificates: public(HashMap[uint256, Certificate])

@external
def __init__():
    self.admin = msg.sender

@external
def issue(_id: uint256, _name: String[16], _course: String[40], _grade: String[1], _date: String[16]):
    assert msg.sender == self.admin, "Not Authorized"
    self.Certificates[_id] = Certificate({ name: _name, course: _course, grade: _grade, date: _date})
    log Issued(_id, _course, _date)

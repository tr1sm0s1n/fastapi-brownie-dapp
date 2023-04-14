from brownie import Cert, accounts, reverts
cert = None


def test_deploy():
    global cert
    cert = Cert.deploy({'from': accounts[0]})
    assert cert.tx.status == 1


def test_issue():
    trx = cert.issue(256, 'Kiefer', 'GOK', 'A', '2031-01-01',
                     '0x2f44454d59535449462f6e6578742d63657274696669636174652d646170702f', {'from': accounts[0]})
    assert trx.events['Issued'].values() == [256, 'GOK', '2031-01-01']


def test_read():
    certificate = cert.Certificates(256)
    assert certificate['name'] == 'Kiefer'
    assert certificate['course'] == 'GOK'
    assert certificate['grade'] == 'A'
    assert certificate['date'] == '2031-01-01'
    assert certificate['document'] == '0x2f44454d59535449462f6e6578742d63657274696669636174652d646170702f'


def test_revert():
    with reverts('Not Authorized'):
        cert.issue(256, 'Mavis', 'GOK', 'S', '2031-01-01',
                   '0x2f44454d59535449462f6e6578742d63657274696669636174652d646170702f', {'from': accounts[1]})
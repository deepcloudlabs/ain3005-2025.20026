import pytest

from banking.account import Account
from banking.bank import Bank

#region accounts
accounts_jack = {
    "tr1": Account("tr1", 100_000),
    "tr2": Account("tr2", 200_000),
    "tr3": None,
    "tr4": None,
    "tr5": None,
    "tr6": None,
    "tr7": None
}
accounts_kate = {
    "tr1": None,
    "tr2": None,
    "tr3": Account("tr3", 300_000),
    "tr4": Account("tr4", 400_000),
    "tr5": None,
    "tr6": None,
    "tr7": None
}
accounts_james = {
    "tr1": None,
    "tr2": None,
    "tr3": None,
    "tr4": None,
    "tr5": Account("tr5", 500_000),
    "tr6": Account("tr6", 600_000),
    "tr7": None
}
#endregion

@pytest.fixture
def a_bank():
    bank = Bank("isbankasi")
    bank.create_customer("1", "jack bauer")
    bank.create_customer("2", "kate austen")
    bank.create_customer("3", "james sawyer")
    return bank


def test_get_account_should_success(mocker):
    bank = Bank("isbankasi")
    jack = bank.create_customer("1", "jack bauer")
    kate = bank.create_customer("2", "kate austen")
    james = bank.create_customer("3", "james sawyer")
    mocker.patch.object(jack, "get_account", side_effect=lambda iban: accounts_jack[iban])
    mocker.patch.object(kate, "get_account", side_effect=lambda iban: accounts_kate[iban])
    mocker.patch.object(james, "get_account", side_effect=lambda iban: accounts_james[iban])
    # 2. call exercise method
    found_account = bank.get_account("tr4")
    # 3. verification
    assert found_account is not None
    assert found_account.iban == "tr4"
    assert found_account == accounts_kate["tr4"]


def test_get_account_should_return_none(mocker):
    bank = Bank("isbankasi")
    jack = bank.create_customer("1", "jack bauer")
    kate = bank.create_customer("2", "kate austen")
    james = bank.create_customer("3", "james sawyer")
    mocker.patch.object(jack, "get_account", side_effect=lambda iban: accounts_jack[iban])
    mocker.patch.object(kate, "get_account", side_effect=lambda iban: accounts_kate[iban])
    mocker.patch.object(james, "get_account", side_effect=lambda iban: accounts_james[iban])
    # 2. call exercise method
    found_account = bank.get_account("tr7")
    # 3. verification
    assert found_account is None
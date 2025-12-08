"""
CUT: Class Under Test -> Account
MUT: Method Under Test
Unit test should follow four test phases:
1. Test Fixture/Setup
2. Call exercise method
3. Verification
4. Cleanup/Teardown

"""
import pytest

from banking.account import Account, AccountStatus

deposit_failure_values =  [-1, -1.10, -0.10, -10]

@pytest.fixture
def an_active_account():
    return Account("TR1", 1_000, AccountStatus.ACTIVE)

@pytest.mark.parametrize("amount",deposit_failure_values)
def test_deposit_with_negative_amount_should_fail(an_active_account,amount):
    # 1. test fixture
    # 3. verification
    with pytest.raises(ValueError):
        # 2. call exercise method
        an_active_account.deposit(amount)

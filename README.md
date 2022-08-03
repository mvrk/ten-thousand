# Ten thousand dice game

This is a command line version of the dice game Ten thousand.
## Author: Rui Guo
## Day I

- Class GameLogic:
- dice_roll(): generate random numbers between 1 to 6.
- calculate_score(): calculate score based on diced numbers according to game rule.
  
### Tests
Test can be running in a python virtual environment. the running command is:
```angular2html
ptw -c -- -k <test_file_name>
```
test files are under ```./tests/version_1``` folder.
- All 47 test passed.(update)
## Day II

- Application should implement all features from previous version
- Application should simulate rolling between 1 and 6 dice
- Application should allow user to set aside dice each roll
- Application should allow “banking” current score or rolling again.
- Application should keep track of total score
- Application should keep track of current round
- Application should have automated tests to ensure proper operation

### Tests
- sims txt using the PyCharm internal "compare with clipboard".
- test files are under ```./tests/version_2``` folder.
- All comparison matched. (updated)
## Day III

- Application should implement features from versions 1 and 2
- Should handle setting aside scoring dice and continuing turn with remaining dice.
 -Should handle when cheating occurs.
- Or just typos. E.g. roll = [1,3,5,2] and user selects 1, 1, 1, 1, 1, 1
- Should allow user to continue rolling with 6 new dice when all dice have scored in current turn.
- Handle zilch: No points for round, and round is over

### Tests
- Test can be running in a python virtual environment. the running command is:
```ptw -c -- -k <test_file_name>```
- sims txt using the PyCharm internal "compare with clipboard".
- test files are under ```./tests/version_3``` folder.

All tests and sims passed.(update)
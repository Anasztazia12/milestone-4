# Testing

## Automated tests

The project uses Django's built-in test framework. Run all tests with:

```text
python manage.py test
```

## Bugs found by the tests

### 1. Site stopped working after pasting code into the wrong file

**Bug:** after adding sorting to the menu, the tests would not run. The error said:

```text
File "bag/views.py", line 5
ImportError: cannot import name 'Category' from 'bag.models'
```

![Test error after pasting into the wrong file](assets/images/test/bag-views-import-error.png)

**Cause:** I pasted the new sorting code into `bag/views.py` instead of `menu/views.py`, so the bag code was replaced.

**Fix:** I used `git restore --source=HEAD~1 bag/views.py` to get the bag code back, and moved the sorting code to `menu/views.py`. More detail is in the Bugs section of the [README](README.md#bugs).

### 2. Homepage favourites test failed after changing the dishes

**Bug:** after I changed the dishes on the homepage, one test failed:

```text
FAIL: test_favourites_show_six_dishes_with_controls (home.tests.HomePageTests)
  File "home/tests.py", line 15, in test_favourites_show_six_dishes_with_controls
    self.assertContains(response, 'class="favourite-card', count=6)
AssertionError: 7 != 6 : Found 7 instances of 'class="favourite-card' (expected 6)

Ran 28 tests
FAILED (failures=1)
```

![Homepage favourites test failing](assets/images/test/home-favourites-test-fail.png)

**Cause:** I replaced Homemade Baby Puree with two dishes, Steak Pie and Beef Steak, so the homepage now has 7 cards. The test still expected 6 cards and the text "Baby Puree".

**Fix:** I updated the test to expect 7 cards and to check for "Steak Pie" instead of "Baby Puree". After the fix all 28 tests passed.

**What I learned:** always run the full `python manage.py test`, not just one app, because a change in one page can break a test in another app.

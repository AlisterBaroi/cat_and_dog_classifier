# Cat & Dog Classifier
Live Link: https://cat-and-dog-classifier-5b4x24knra-uc.a.run.app/

![image](https://github.com/AlisterBaroi/cat_and_dog_classifier/blob/c011b26cadaf6047329622a6730a4a6de8ee107f/.github/workflows/demo.png)


## Branch Metodology
Create new branch from `main` branch, work on the code, and PR to `staging` branch. Once all the CI tests run successfully, the `staging` will auto PR to `main`. The diagram below illustrates the flow:

```mermaid
  graph TD;
      A[main] -- 1. Create new from main --> B[new-branch];
      C[staging] -- 3. If CI tests pass --> A[main];
      C[staging] -- 4. If CI tests fail --> B[new-branch];
      B[new-branch] -- 2. PR to staging --> C[staging];
```
Note: The `main` and `staging` branches are protected (and deletion protected), you cannot directly commit or PR to the `main` branch. The only way to commit to `main` is to PR to `straging`. If the CI tests on `staging` passes, then the admin can do PR from `staging` to `main`. But, if the CI tests fail, you need to review the code, for we cannot PR to `staging`, thus cannot PR to `main` from `staging`.

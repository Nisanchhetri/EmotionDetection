# Analysis

## Problem Formulation

| Problem Formulation          |                                                                                                                                                                       |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                         | We want a model that can predict the emotions("Sad", "Excited", "Angry", "Fear" and "Happy") from the customer product for further analysis, such as happiness index. |
| Experience                   |From product reviews \| Using ISEAR dataset consisting of 5 emotions label with 7446 samples.                                                                                                 |
| Performance                  | Weighted accuracy of the classification \| Revenue Generated \| Customer satisfaction                                                                                 |
| Reason to solve              | The output will be used to provide better customer e-commerce experience and increase sales revenues                                                                  |
| Success Criteria             | It's a success if customer satisfaction increased by 30%, increase in accuracy than "SenseMotion" more than 20%, and revenues increased by 15%                        |
| Other metric of interest are | Precision of classification                                                                                                                                           |

## Solution Formulation

| Solution Formulation |                                                                                                                                                                                  |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Manual solution      | - A mandatory emotion rating on the product review can give an estimation of emotion.<br>- Dividing the review into smaller sections for manual review. (Using Humans)(n-gram??) |
| As ML Task           |  NLP Classification task \| Text analysis \| Review Clustering                                                                                                                      |
| Similar Task         | - Sentiment Analysis.<br>- Any NLP classification task.<br>- Emotion clustering task.                                                                                            |
| Reason to solve      | The output will be used to provide better customer e-commerce experience and increase sales revenues                                                                             |
| Assumptions          | Words/sentence in the document carries the essence of the customer's emotion.                                                                                                    |
| Baseline model       | Treat as multiclass-classification conducted using Artificial neural network.                                                                                                    |

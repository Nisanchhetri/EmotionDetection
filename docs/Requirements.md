#  Company Overview

| Client:             | Emoticon Pvt. Ltd.                                                                                        |
|---------------------|-----------------------------------------------------------------------------------------------------------|
| Contact Person:     | Sweekar Piya<br>Email : piyasweekar@gmail.com<br><br>Nisan Chhetri<br><br>Email: nisanchhetri50@gmail.com |
| Address:            | NC State, USA                                                                                             |
| Project Start Date: | May 7                                                                                                     |
| Employee:           | 100                                                                                                       |
| Products:           | BuyStop - Buy/sell Product website like Ebay and Amazon.                                                  |
| Project Deadline:   | May 19 (9-10 Days)                                                                                        |

**Project Objective:**

Extract consumer’s emotion from reviews on products through RESTful API for understanding and providing better customer experience.

## About the Company

Q.1 Tell me about your business, mission, vision and the domain it operates in.

-   startup company, consist of 100 employees with 6 departments sales, operations, technology, HR, QA/QC and admin and logistics. (Has QC department for checking dataset quality).
    
-   Domain: E-commerce.
    

  

Q.2 Describe your mission and vision.

-   Mission: At Emoticon, our mission is to provide a global online marketplace for buying and selling products with phenomenal customer service.
    
-   Vision: Our vision is to provide the best consumer experience on online marketplaces.
    

  

Q.3 What are the products and services that you provide?

-   Currently with a single product named “BUYSTOP”, which is an ecommerce website for buying and selling goods like Ebay.

## Context on the product

Q.1 Why is the system required? Where does the product fit in your business?

We require this emotion detection system,

1.  Recognizing the current happiness index of consumers to gauge how well the ecommerce website is performing.
    
2.  Recognizing if any consumers are suffering from anxiety/depression and provide them special services such as exclusive discounts.
    
3.  Recognize the consumer satisfaction/dislikes of purchased products.
    
4.  Redirecting advertisement in accordance with the emotion of the consumers.
    

  

Q.2 Is there any system present to conduct such services of emotion detection? From any competitors?

Ans: Multiple sentiment analysis products are available such as [Sentiment analysis](https://github.com/kampaitees/Sentiment-Analysis). However, we required deeper classification of emotion.

  

Yes, there is a product named “__SenseMotion__” is available and uses vanilla neural networks for detection of emotions(sad, disgust and happy) from text. It is said to have pretty low accuracy of about 40%.

  

Q.3 What features do you like and dislike about “Buystop”?

__Likes__

-   Aesthetically appealing.
    
-   Mandatory review section during each purchase.
    
-   Provides recommendation to customers regarding complementary products after purchase.
    

__Dislikes__

-   Not enough clicks on the advertisement provided.
    
-   No way to recognize the satisfaction of buying a product. (having this enable better advertisement).
    
-   Manual reviewing of comments on the product is required for emotion analysis(want automation).
    

  

__Pain Points__

-   Manual emotion analysis resulting in huge time consumption and extra manpower.
    
-   No methodology of knowing the average happiness index of the consumers causing degradation of sales.

## About the new product

Q.1 What are the essential/non-essential needs of the project?

| Essential                                                                                                                             | Non-Essential                                                                                                                 |
|---------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Must use Python programming language. (Django or  flask for backend)                                                                  | Logs of the developing model.(should  have)                                                                                   |
| Must train and classify emotion among 5 categories"Sad", "Excited", "Angry", "Fear" and "Happy" using the dataset provided.           | Engineer the dataset using Part of speech tags, n-grams for increasing the accuracy(could have)                               |
| API for returning the emotion given consumer’s review comment.                                                                        | Incorporate happiness index calculation in real time and alert when it reaches below the standard..(If possible, could haves) |
| Requires more precise classification rather than classifying all the reviews.( Better precision of classification rather than recall) | Reproducibility at client’s side(Docker container)                                                                            |

Q.2  What benefit can the product provide for your customers?

-   Decrease in sadness by providing discounts to the customers.
    
-   Improvement in customer service through recognition of emotion.

Q.3 Specific acceptance criteria for the system.

-   Use weighted accuracy as the metric for the result since the ratio of samples for each class isn’t similar. Required at least 20% increment in accuracy than __SenseMotion__. Note, the prediction must be precise rather than having better recall.

Q.4 What are the functional and non-functional requirements?

__Functional__

-   Emotion detection
    
-   Must use REST API

__Non-functional__

-   Scalable to larger dataset
    
-   Reliability of classification
    
-   Applicable for other dataset.

## System Usage

Q.1 Which of your staff will be using or involved in the product the most?

-   Tech team is the main staff who are involved for most part, they are the one providing the dataset and deploying the system later in BuyStop. Communicating with them is crucial.

Q.2 Do we need to know of any other software that is integrated with the system?

-   Just required to develop a working ML model and REST API for classification. No extra software.

## About the Data

Q.1 Do your company have any sort of data that is related to the system? Do you have the text dataset of reviews?

-   Company’s data is confidential. We should use the available [ISEAR](https://drive.google.com/file/d/12jwlbgKEASZ8kKLZ1Q7mAkxuhHM_AKB0/view) dataset consisting of 5 emotions with 7446 samples.

Q.2 Any special team for data infrastructure management?

-   Startup company - No team of data engineers.

Q.3 How is data stored?

-   Confidential

## Caveats

Q.1 What are the main constraints of the system being built?

-   The timing of the system development is very precise. The project must be wrapped up in 9-10 days.
    
-   The training must be optimized as much as possible for fast automation and emotion detection.

Q.2 Have you thought about any future upgrades regarding the system?

-   No right now, we just hope scalability in the system developed such that we can train the system later in our data.
## General

Q.1 Do you have any concrete timeline for the system development?

-   About 9 days with progress reporting on day 6 and final reporting on 9.

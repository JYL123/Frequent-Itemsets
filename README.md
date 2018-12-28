## Looking for Frequent Itemsets in Chinese

### Text segamention
`Text segamentation` is dividing sentences into its meaningful components. It is a subject of `natural language processing`. In some languages, such as English, `white space` is a good delimiter to divide text into its individual parts, even though it has its limitations in the case of `collocations` and `compounds`. However, in many other languages, such as Chinese and Japanese, there is no white space between the words, except when there is a presence of punctuation. For more information, you can refer to [this link.](https://en.wikipedia.org/wiki/Text_segmentation) In this project, we will make use of [jieba](https://github.com/fxsjy/jieba) this segamentation module to segment Chinese text. 

### Frequent itemsets
Frequent itemsets are sets of items associated with each other. This problem of discovering frequent itemsets can be viewed as a subfield of discovering of association rules, which is often more complex. 

In this project, we will use `market-basket` model of data, which is a model of `baskets`, sometimes is referred as `transctions`, with each basets contaning many `items`. So each basket consists of a set of items, and data consists of a seuence of baskets. Here we are intertested in finding ut the absolute number of basekts that contain a particular set of items, and we will define `frequent` basing on those numbers. 

`Frequent`: a set of items that appear in many baskets. We assume that there is a number `s`, called the `support threshold`. If `I` is a set of items, the `support` for `I` is the number of baskets for which `I` is a subset. We say `I` is `frequent` if its support is `s` or more. With this concept, we can discover frequent singleton (with 1 item each subset) frequent doubleton (2 items each subset), frequent triplet (3 items eac subset) for given data. The underlying rule is that, a doubleton cannot be frequent unless both items in the set are frequent by themselves. In order to be a frequent triple, each pair of elements in the set must be a frequent doubleton. This rule can be easily seen from a table which we plots our support result. 


### A-priori Algorithm
The association rules is of the form: `I->j`, where `I` is a set of items and `j` is an item. The implication of this association rule is that if all of the items in I appear in some basket, then `j` is "likely" to appear in that basket as well. The notion of "likely" by defining the `confidence` of the rulw `I->j`, the `confidence` is defined to be the ration of the support for `I AND {j}` to the support for `I`. That is the confidence of the rule is the fraction of the baskets with all of `I` that also contain `j`. `Confidence` alone can be useful, provided the support for the left side of the rule is fairly large.

THere is more value to an association rule if it reflects a true relationship, where the item or items on the left somehow afect the item on the right. We define the `interest` of an association rule `I->j` to be the difference between its confidence and the fraction of baskets that contain `j`. That is, if `I` has no influence on `j`, then we would expect that the fraction of baskets including `I` that contains `j` would be exactly the same as the fraction of all baskets that contains 
`j`.

Frequent itemsets can be defined as sets of items that has association rules with high support and confidence.

### Question

The problem encountered in this algorithm is how to sort pairs of Chinese characters.




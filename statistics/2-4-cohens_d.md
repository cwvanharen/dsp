[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)


```
import thinkstats2
import nsfg
import math


df = nsfg.ReadFemPreg()
totalwgt_lb = df['totalwgt_lb']
total_mean = totalwgt_lb.mean()
first = totalwgt_lb[df.birthord == 1]
others = totalwgt_lb[df.birthord != 1]
first_mean = first.mean()
others_mean = others.mean()
print total_mean
print first_mean
print others_mean

7.26562845762
7.20109443044
7.32585561497
```

>> A quick look at the means shows some evidence that first babies are lighter than subsequent babies. However, it's hard to tell if the effect size is meaningful here - neither is far from the total mean. Computing Cohen's d gives us one way to quantify the difference, stating it in terms of the pooled standard deviations.

>>This code computes Cohen's d and prints out a few sanity checks on the way.

```
def cohen(pop_a, pop_b):
    mean_a = pop_a.mean()
    mean_b = pop_b.mean()
    print 'mean a: ', mean_a
    print 'mean b: ', mean_b
    var_a = pop_a.var()
    var_b = pop_b.var()
    print 'StDv: ', math.sqrt(var_a), math.sqrt(var_b)
    a_n = len(pop_a)
    b_n = len(pop_b)

    pooled_var = (a_n * var_a + b_n * var_b) / ( a_n + b_n)
    d = (mean_a - mean_b) / (math.sqrt(pooled_var))
    return d
print cohen(first, others)

mean a:  7.20109443044
mean b:  7.32585561497
StDv:  1.42057287772 1.39419547621
-0.0889364117772
```

>> So the difference in means is about .089 standard deviations. The difference in pregnancy lengths was .029, this effect size is three times that, *however*, the difference is less than a tenth of one standard deviation so it's still a pretty small difference.

[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

```
import scipy.stats

mean = 178
sd = 7.7
men = scipy.stats.norm(loc=mean, scale=sd)
men.cdf(185.4) - men.cdf(177.8)
```
So about 34% of U.S. men are between 5'10"(177.8cm) and 6'1"(185.4cm) assuming a perfectly normal distribution.
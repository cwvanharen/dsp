[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)


```
%matplotlib inline

import random
import thinkplot
import thinkstats2

random_list = [random.random() for i in range(1000)]
pmf = thinkstats2.Pmf(random_list)

thinkplot.Pmf(pmf, linewidth=0.1, label='Random?')
thinkplot.Show()
```
![Pmf](https://github.com/cwvanharen/dsp/blob/master/statistics/RandomPmf.png?raw=true)
```
cdf = thinkstats2.Cdf(random_list)

thinkplot.Cdf(cdf, label='Random?')
thinkplot.Show()
```
![Cdf](https://github.com/cwvanharen/dsp/blob/master/statistics/RandomCdf.png?raw=true)

The Pmf doesn't tell us much, but the Cdf gives us a better idea of whether random.random is uniform. With a thousand values the Cdf is almost a straight line so the distribution is at least close to uniform.
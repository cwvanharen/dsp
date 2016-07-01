[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)


```
%matplotlib inline

import chap01soln
import thinkstats2
import thinkplot

resp = chap01soln.ReadFemResp()
actual_pmf = thinkstats2.Pmf(resp.numkdhh)

biased_pmf = actual_pmf.Copy()

for x, p in actual_pmf.Items():
    biased_pmf.Mult(x, x)

biased_pmf.Normalize()

#thinkplot.Pmf(actual_pmf, label='Actual Kid Pmf')
#thinkplot.Show()
thinkplot.PrePlot(2)
thinkplot.Pmfs([actual_pmf, biased_pmf])
thinkplot.Show()
```
![Biased vs Actual](https://github.com/cwvanharen/dsp/blob/master/statistics/ActualvBiased.png?raw=true)
```
print biased_pmf.Mean()
print actual_pmf.Mean()
2.40367910066
1.02420515504
```
Clearly if we weight the distribution by oversampling in proportion to the values we end up with a very different, very biased result.
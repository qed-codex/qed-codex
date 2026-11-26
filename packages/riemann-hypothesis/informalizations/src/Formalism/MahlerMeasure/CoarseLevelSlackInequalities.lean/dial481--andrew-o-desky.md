---
{
  "module": "src/Formalism/MahlerMeasure/CoarseLevelSlackInequalities.lean",
  "declarations": [
    "Formalism.GM.Top.windowCountAP",
    "Formalism.GM.Top.windowFullAP"
  ],
  "author": "dial481",
  "writer": "Andrew O'Desky",
  "origin": "other-author",
  "source": "https://andrewodesky.com/rh/",
  "source_commit": "40e56bab026552e089d7afcfeff08d2defb9c005",
  "license": "with-permission"
}
---

As published on 26 November 2026.

## Averaging small invariant factors along an arithmetic progression

[Theorem PHT.0397](https://andrewodesky.com/rh/lean/Formalism.GM.Top.windowFullAP/)

Let $p$ be prime and $K$ an ultrametric normed field with an isometric normed $\mathbb Q_p$-algebra structure. Let $n,\delta,h\ge0$, $1\le Y\le p^h$, $\delta\le p^h$, $E>0$, and $\Lambda\in\mathbb R$. Choose coefficients $c_{ijk}\in K$ with $|c_{ijk}|\le1$ and form $$B(T)_{ij}=\sum_{k=0}^{\delta}c_{ijk}{T\choose k}.$$ Assume $\det B(T)=a\prod_{\zeta\in Z}(T-\zeta)$ for $a\ne0$ and a multiset $Z$ in $K$, with $$-\log_p|a|+\frac{|Z|}{p-1}\le n\Lambda.$$ Let $t_0,d\in\mathbb Z$ with $\gcd(d,p)=1$. For every $t=t_0+dj$, $0\le j<Y$, suppose $$B(t)=U_t\operatorname{diag}(b_{t,1},\ldots,b_{t,n})V_t,$$ where all entries of $U_t,V_t$ have absolute value at most one and $|\det U_t|=|\det V_t|=1$. Then $$\frac1Y\sum_{j=0}^{Y-1}\#\{i:|b_{t_0+dj,i}|\le p^{-E}\}\le n\left(\frac\delta Y+\frac{\Lambda+\delta h/Y}{E}\right).$$

## Truncated valuations along a prime-to-p progression

[Theorem PHT.1075](https://andrewodesky.com/rh/lean/Formalism.GM.Top.windowCountAP/)

Let $p$ be prime and $K$ an ultrametric normed field equipped with a normed $\mathbb Q_p$-algebra structure. Let $\zeta\in K$, $t_0,d\in\mathbb Z$ with $\gcd(d,p)=1$, and $Y,h\ge0$ integers. Then $$\sum_{j=0}^{Y-1}v_h(t_0+dj-\zeta)\le\sum_{i=1}^{h}\left(\frac{Y}{p^i}+1\right),$$ where $$v_h(x)=-\log_p\max(|x|,p^{-h}).$$

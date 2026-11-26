---
{
  "module": "src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/ShortGeneratorNormComparison.lean",
  "declarations": [
    "GlobalTheory.T.short_generator_norm_comparison"
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

## Uniform bounds for generators of integral cusp-form lattices

[Theorem ARAK.1533](https://andrewodesky.com/rh/lean/GlobalTheory.T.short_generator_norm_comparison/)

Assume ([Global hypotheses for Hodge-bundle estimates](https://andrewodesky.com/rh/s/k2-hodge-bundle-hypotheses.html)). There is $C\ge0$ with the following property, uniform in the arithmetic and automorphic data. Fix its complete family datum and comparison laws, with CM field $E$, integer parameters $f,r,m$, and a stage $1\le j\le m$ whose signature $(p,q)$ has $p,q\ge1$, with $[E:\mathbb Q]/2>2$. Choose a covered moduli datum satisfying the source's good-cover conditions with parameters $e\ge0$, $o\in\mathbb R$ and level integer $M$. For a number field $K$, put $$s(K)=\log[K:\mathbb Q]+\frac{\log|\operatorname{disc}K|}{[K:\mathbb Q]}.$$ Let $L\ge1$ satisfy $$\log M\le30L,\quad s(E)\le3L,\quad\log(fr)\le L,\quad o\le391(frL)^2.$$ Suppose the associated flat sections exist on every compatible compactification and embedding, all have arithmetic degree $-c_1$, and $|c_1|\le9rL$. Let $\lambda_{\tau,k}$ be an integral weight on the stage's prescribed embedding and weight-index sets, decreasing weakly in $k$ for every $\tau$, with $$\lambda_{\tau,p}-\lambda_{\tau,p+1}\ge8fr+10,\qquad \log S\le10L,\qquad S=\sum_\tau\sum_k|\lambda_{\tau,k}|.$$ For every compatible compactification $Z$, the integral cusp-form lattice $\Lambda_Z(\lambda,0)$ has generators $w_1,\ldots,w_n$ over $\mathbb Z$ and a bound $B\ge1$ such that all the prescribed comparison norms of every $w_i$ are at most $B$, and $$\log B\le C\bigl((frL)^3S+(frL)^5\bigr),\qquad\log n\le C(frL)^3.$$ The real logarithm has value zero at zero.

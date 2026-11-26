---
{
  "module": "src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/IntegralCuspSlopePowerBound.lean",
  "declarations": [
    "UpperTheory.Lit.Tam.tamagawa_number_formula"
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

## Uniform Bergman and evaluation bounds for cusp forms

[Theorem ARAK.0065](https://andrewodesky.com/rh/lean/UpperTheory.Lit.Tam.tamagawa_number_formula/)

Assume the source's published Hodge-bundle theorem package. Fix the full arithmetic datum specified in ([The convergent doubling integral identity](https://andrewodesky.com/rh/lean/GlobalTheory.T.doubling_basicIdentity_unfolding/)) with rank parameters $f,r$, a compatible system of moduli and cusp-form realizations satisfying its core laws, and a stage $1\le j\le m$, where $m$ is the datum's number of stages, with both signature entries at least one. Let $E$ be the CM field and suppose $[E:\mathbb Q]/2>2$. Let $Y$ be a deeper-level realization satisfying the full uniformization and metric conditions at parameters $e\ge0$ and $o\in\mathbb R$. Write $M$ for its level-size integer and put $$s(K)=\log[K:\mathbb Q]+\frac{\log|\operatorname{disc}K|}{[K:\mathbb Q]}.$$ There is a universal $C\ge0$ such that, whenever $L\ge1$ and $$\log M\le30L,\quad s(E)\le3L,\quad\log(fr)\le L,\quad o\le391(frL)^2,$$ for every integral weight $\lambda$ decreasing weakly at each embedding, with $$\log\left(\sum_{\tau,i}|\lambda_{\tau,i}|\right)\le20L,$$ and every component $Z$, the Bergman function is at most $\exp(C(frL)^3)$ on the prescribed frames of $Z$, and every cusp form $v$ satisfies $$\|v(z)\|_{\mathrm{point}}^2\le e^{C(frL)^3}\|v\|_{\mathrm{Pet}}^2,\qquad \log\operatorname{rank}_Z(\lambda)\le C(frL)^3.$$ The point norm, Petersson norm, Bergman function and rank use the fixed metric, volume and uniformization dictionary of $Y$.

---
{
  "module": "src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/SlopeIneqMean.lean",
  "declarations": [
    "Formalism.HN.slope_inequality_mean"
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

## Slope bound for the image of a map

[Theorem ARAK.0119](https://andrewodesky.com/rh/lean/Formalism.HN.slope_inequality_mean/)

Let $K$ be a totally complex number field. Let $A$ be a finitely generated $\mathcal O_K$-submodule of a finite-dimensional Hermitian $K$-space and let $\varphi$ be a $K$-linear map to another such space, with $\varphi(A)\ne0$. Write $\mu$, $\mu_{\min}$, and $\mu_{\max}$ for the mean and extreme Harder–Narasimhan slopes, using the extremal definitions in ([Characterization and attainment of extreme lattice slopes](https://andrewodesky.com/rh/lean/Formalism.HN.slope_characterization/)) with the normalization below. Use $\mu(A)=-2\log\operatorname{covol}(A)/([K:\mathbb Q]\operatorname{rk}A)$, with discriminant-normalized covolume and the same squared-norm normalization for the extreme slopes. Let $r_2(K)$ be the number of complex places and let $\|\varphi\|_v$ be the operator norm at $v$. Define the height by $$h(\varphi)=\frac1{r_2(K)}\sum_{v\mid\infty}\log\|\varphi\|_v^2.$$ Then $$\mu_{\min}(\varphi(A))\ge\mu_{\min}(A)-h(\varphi).$$ For any finitely generated target submodule $B\supseteq\varphi(A)$, $$\mu_{\min}(A)\le\mu_{\max}(B)+h(\varphi).$$ If $\varphi$ is injective on $A$, also $\mu_{\max}(A)\le\mu_{\max}(B)+h(\varphi)$.

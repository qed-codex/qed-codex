---
{
  "module": "src/Formalism/HermitianCurvature/HermitianCurvatureProofs/PairingTriangular.lean",
  "declarations": [
    "Formalism.FourierDecayAlt.P.latticeHerglotzBound_statement"
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

## A lattice sum bound with a positive definite Fourier correction

[Theorem ANT.1096](https://andrewodesky.com/rh/lean/Formalism.FourierDecayAlt.P.latticeHerglotzBound_statement/)

Let $V=\mathbb C^f$, $\Lambda\subseteq V$ a discrete full $\mathbb Z$-lattice, and put $$e(z)=\exp\!\left(2\pi i\sum_{v=1}^f(z_v+\bar z_v)\right),\qquad\Lambda^*=\{\sigma:e(\sigma z)=1\text{ for all }z\in\Lambda\},$$ where $\sigma z$ is the coordinatewise product. Let $N:V\to\mathbb R$ be nonnegative, lower semicontinuous and Lebesgue integrable, and let $A:V\to\mathbb C$ satisfy $$\operatorname{Re}\sum_{\sigma,\sigma'\in T}A(\sigma-\sigma')c_\sigma\overline{c_{\sigma'}}\ge0$$ for every finite $T\subseteq\Lambda^*$ and complex coefficients $c_\sigma$. Define $\widehat N(\sigma)=\int_V N(z)e(\sigma z)\,dz$ and assume $\sum_{\sigma\in\Lambda^*}|\widehat N(\sigma)+A(\sigma)|<\infty$. Then for every $z_0\in V$ and finite $S\subseteq z_0+\Lambda$, $$\operatorname{covol}(\Lambda)\sum_{z\in S}N(z)\le\sum_{\sigma\in\Lambda^*}|\widehat N(\sigma)+A(\sigma)|.$$

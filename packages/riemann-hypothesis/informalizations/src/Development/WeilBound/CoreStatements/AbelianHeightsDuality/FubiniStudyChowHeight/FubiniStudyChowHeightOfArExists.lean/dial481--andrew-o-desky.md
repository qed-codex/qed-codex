---
{
  "module": "src/Development/WeilBound/CoreStatements/AbelianHeightsDuality/FubiniStudyChowHeight/FubiniStudyChowHeightOfArExists.lean",
  "declarations": [
    "FubiniStudyChowHeightFormula₂.Fs.stMain"
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

## Arithmetic self-intersection and Chow height

[Theorem ARAK.0053](https://andrewodesky.com/rh/lean/FubiniStudyChowHeightFormula%E2%82%82.Fs.stMain/)

Let $K$ be a number field, $m,e\ge0$, and $Z$ an integral projective $\mathcal O_K$-scheme, flat over $\mathbb Z$, of dimension $e+1$. Let $\overline L$ be a smooth Hermitian line bundle on $Z$ and $s_1,\ldots,s_m$ sections generating $L$. Assume each open $\{s_i\ne0\}$ is affine and its coordinate ring is generated over $\mathcal O_K$ by the ratios $s_j/s_i$.

For each embedding $\sigma:K\hookrightarrow\mathbb C$, choose an invertible matrix $M_\sigma$ defining $\|u\|_\sigma=\|M_\sigma u\|_2$, with $\|\bar u\|_{\bar\sigma}=\|u\|_\sigma$. Assume the metric of $L$ is the Fubini–Study metric defined by these sections and the dual norms $\|y\|_\sigma^*=\|(M_\sigma^t)^{-1}y\|_2$. Let $f$ be a Chow form of the homogeneous ideal of the generic image, in $e+1$ blocks of $m$ variables, homogeneous of degree $\delta$ in each block. Define $$h(f)=\frac1{[K:\mathbb Q]}\left(\sum_{v\text{ finite}}\log\max_\alpha|f_\alpha|_v+\sum_\sigma\left(\int\log|f^\sigma(u_0,\ldots,u_e)|\,d\mu_\sigma+\frac{(e+1)\delta}{2}\sum_{j=1}^{m-1}\frac1j\right)\right),$$ where $f_\alpha$ are the coefficients, the finite absolute values are normalized by $|\varpi_v|_v=(Nv)^{-1}$, and $\mu_\sigma$ is the product of the sphere probability measures induced by radial projection from the $\|\cdot\|_\sigma$ unit ball. If the arithmetic self-intersection of $\overline L$ exists and equals $a$, then $$a=[K:\mathbb Q]h(f).$$

---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FlagMeasures/CovolumeIntegralUnipotentRadicalRealPointsStatement.lean",
  "declarations": [
    "GlobalTheory.T.covolume_integral_unipotentRadical_real_points"
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

## Covolume of an integral flag-unipotent group

[Theorem ANT.0309](https://andrewodesky.com/rh/lean/GlobalTheory.T.covolume_integral_unipotentRadical_real_points/)

Let $E/F$ be a CM extension with conjugation $\sigma$ and assume $\mathcal O_E/\mathcal O_F$ is formally unramified. Let $k,r\ge0$, $N=2r+k+1$, and let $J\in M_N(E)$ be nondegenerate Hermitian. Let $\Lambda\subset E^N$ be a finitely generated self-dual $\mathcal O_E$-module for $J$. Choose $T\in F$ and matrices $P=(p_0,\ldots,p_r)$, $f=(f_0,\ldots,f_{r-1})$ with independent columns of $P$ and $$P^*JP=\operatorname{diag}(0,\ldots,0,-T),\qquad P^*Jf=\begin{pmatrix}I_r\\0\end{pmatrix},\qquad f^*Jf=0.$$ Writing $\mathfrak D_E$ for the absolute different, assume $$\mathfrak D_E^{-(r-b)}p_b\subseteq\Lambda\quad(0\le b\le r),\qquad\mathfrak D_E^{r-b}f_b\subseteq\Lambda\quad(0\le b<r).$$ Let $H$ be the standard Hermitian matrix specified below. For every infinite place $w$ of $E$, choose $A_w\in M_N(\mathbb C)$ with $A_w^*HA_w=w(J)$. Suppose $s_0,\ldots,s_{r-1}>0$ satisfy $$A_ww(p_b)=s_be_b,\qquad A_ww(f_b)=s_b^{-1}e_{N-1-b}\quad(0\le b<r).$$ Put $e=(p_0,\ldots,p_{r-1})$. Let $\Gamma$ consist of matrices $\gamma\in U(J)(E)$ preserving $\Lambda$ such that $\gamma e=e\nu$ for some upper unitriangular $\nu$, and $(\gamma-I)e^\perp\subseteq\operatorname{span}_Ee$. There exists a measurable set $\mathcal D\subseteq\prod_{w\mid\infty}M_N(\mathbb C)$ such that for each $x=(x_w)\in\prod_wN_H$ there is exactly one $\gamma\in\Gamma$ with $(A_ww(\gamma)A_w^{-1}x_w)_w\in\mathcal D$. Every measurable set with this property has volume $$|\operatorname{disc}F|^{-(k+1)r^2-4(r^3-r)/3-3r/2}\left(\prod_{b=0}^{r-1}s_b^{4(r-b)+2k}\right)^{[F:\mathbb Q]}.$$

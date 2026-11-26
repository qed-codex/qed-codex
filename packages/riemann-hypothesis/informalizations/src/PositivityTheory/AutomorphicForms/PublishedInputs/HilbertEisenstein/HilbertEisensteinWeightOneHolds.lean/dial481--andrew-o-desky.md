---
{
  "module": "src/PositivityTheory/AutomorphicForms/PublishedInputs/HilbertEisenstein/HilbertEisensteinWeightOneHolds.lean",
  "declarations": [
    "UpperTheory.V.Published.hilbert_eisenstein_weight_one_holds"
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

## A weight-one Hilbert form with divisor-sum coefficients

[Theorem ANT.0049](https://andrewodesky.com/rh/lean/UpperTheory.V.Published.hilbert_eisenstein_weight_one_holds/)

Let $F$ be a totally real number field and $\omega$ a finite-order Hecke character of $F$. Assume $\omega_v(-1)=-1$ at every infinite place. Let $c_w$ be its conductor exponent at each finite place $w$, and assume $c_w\ne0$ for at least one $w$. For an integral ideal $\mathfrak r$, define $$\omega_c(\mathfrak r)=\prod_w\alpha_w^{\operatorname{ord}_w\mathfrak r},\qquad \alpha_w=\begin{cases}\omega_w(\varpi_w),&c_w=0,\\0,&c_w\ne0,\end{cases}$$ where $\varpi_w$ is the fixed local uniformizer and $0^0=1$. There are a smooth holomorphic automorphic form $\phi$ on $\mathrm{GL}_2(\mathbb A_F)$ of parallel weight $1$, central character $\omega$, fixed by $K_1(\mathfrak p_w^{c_w})$ at every finite $w$, and a constant $L\in\mathbb C$ whose normalized Fourier expansion has constant term $L$ and ideal coefficients $$a(\mathfrak m)=\sum_{\mathfrak r\mid\mathfrak m}^{\mathrm{fs}}\omega_c(\mathfrak r).$$ Here the sum is the usual finite divisor sum for $\mathfrak m\ne0$; the superscript specifies the convention of summing a function with finite nonzero support, and returning zero if that support is infinite. The product defining $\omega_c$ has value one if its nonidentity factors have infinite support.

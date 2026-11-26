---
{
  "module": "src/Formalism/DistinguishedUnitIdeals/DistinguishedOrderProofs/LemmaC.lean",
  "declarations": [
    "Formalism.ExponentWindows.lemma_C_valuation_real"
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

## A valuation bound from an ideal relation between distinguished powers

[Theorem PHT.1005](https://andrewodesky.com/rh/lean/Formalism.ExponentWindows.lemma_C_valuation_real/)

Let $O$ be a discrete valuation ring with uniformizer $\varpi$, and let $\ell\ge2$, $e\ge1$ be integers such that $\ell$ and $\varpi^e$ are associated in $O$. For each $s\ge0$, let $E_s\in O[T]$ be monic of degree $\ell^s$, with every coefficient below its leading coefficient divisible by $\ell$, and with constant coefficient associated to $\ell$. Choose units $u_s\in O[[T]]$ and put $V_s=u_sE_s$.

Let $h,g,a,b_0,b_1,s_0,s_1,k\ge0$, with $$s_0<s_1,\qquad 2(a+2gh)<b_1,\qquad 2b_0\le\ell b_1.$$ If $$\ell^a\left(\prod_{s=0}^{h-1}V_s^g\right)^2V_{s_0}^{b_0}\in(\varpi^k,V_{s_1}^{b_1})\subset O[[T]],$$ then $$k\le e\,\frac{(a+2gh)b_1}{b_1-b_0/\ell},\qquad k\le2e(a+2gh).$$

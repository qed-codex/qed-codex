---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/FontaineDcris.lean",
  "declarations": [
    "GlobalTheory.Per.DcrisExact.exactStrict"
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

## Exactness and strictness of crystalline periods

[Theorem PHT.0680](https://andrewodesky.com/rh/lean/GlobalTheory.Per.DcrisExact.exactStrict/)

Let $l$ be prime and fix the local period datum, integral period-ring datum and compatible identifications with the crystalline and de Rham rings in ([De Rham subrepresentations and strict quotient maps](https://andrewodesky.com/rh/lean/GlobalTheory.DRSubQuot.deRham_sub_quot/)). Let $K,L\subset\overline{\mathbb Q}_l$ be finite extensions, and suppose the scalar map $K_0\to K$ is bijective, where $K_0$ is the maximal unramified subfield. Let $$0\longrightarrow V_0\xrightarrow{\iota}V_1\xrightarrow{\pi}V_2\longrightarrow0$$ be an exact sequence of finite-dimensional $L$-linear representations of $G_K$, with equivariant $L$-linear maps and compatible $\mathbb Q_l$-scalar structures. If all three representations are crystalline, the induced sequence of crystalline period modules is exact. For every integer $a$, $$\pi_*(\operatorname{Fil}^aD_{\mathrm{cris}}(V_1))= \operatorname{Fil}^aD_{\mathrm{cris}}(V_2),$$ $$\operatorname{Fil}^aD_{\mathrm{cris}}(V_0)= D_{\mathrm{cris}}(V_0)\cap\iota_*^{-1} (\operatorname{Fil}^aD_{\mathrm{cris}}(V_1)).$$

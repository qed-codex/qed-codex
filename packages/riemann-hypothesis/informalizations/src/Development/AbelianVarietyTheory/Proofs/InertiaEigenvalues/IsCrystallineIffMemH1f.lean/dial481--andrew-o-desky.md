---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/IsCrystallineIffMemH1f.lean",
  "declarations": [
    "GlobalTheory.CrysExt.isCrys_iff_surjective"
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

## A crystalline extension criterion by surjectivity on periods

[Theorem PHT.0867](https://andrewodesky.com/rh/lean/GlobalTheory.CrysExt.isCrys_iff_surjective/)

Let $(k,K_0,K,B,B_{\mathrm dR})$ be a period-data package for a group $G$ as specified below, and let $L/k$ be a finite field extension. For an $L$-representation $V$, put $$D_B(V)=(V\otimes_kB)^G,$$ and call $V$ crystalline when $\dim_L D_B(V)=[K_0:k]\dim_LV$. Let $V$ be finite-dimensional and crystalline, and let $$0\longrightarrow V\xrightarrow{i}W\xrightarrow{p}L\longrightarrow0$$ be an exact sequence of $L$-representations, with trivial action on $L$. Then $$W\text{ is crystalline}\quad\Longleftrightarrow\quad D_B(p):D_B(W)\longrightarrow D_B(L)\text{ is surjective}.$$

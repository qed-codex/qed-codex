---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FlagMeasures/HermitianDoubleCosetAmplitudeBoundLocalStatement.lean",
  "declarations": [
    "GlobalTheory.T.hermitianDoubleCoset_amplitude_bound_local"
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

## Second moments of local Hermitian amplitudes

[Theorem REP.1222](https://andrewodesky.com/rh/lean/GlobalTheory.T.hermitianDoubleCoset_amplitude_bound_local/)

Let $C\ge39$. Fix the source's local-field model, satisfying its full model conditions, and a Hermitian space $V$ in that model. Let $P$ be a pair of framed rank-$r$ decompositions satisfying its relative-position conditions at the model's additive-character parameter. Suppose $k,r\ge0$, $4r+7\le k$, and $\dim_EV=k+2r+1$.

For any representatives $\mathcal D$ for the associated lattice data and representatives $\mathcal T_d$ for the terms above each $d\in\mathcal D$, fix an initial datum $d_0$. Write $\mu(t)$ for the term's volume, $\omega(t)$ for its complex character factor, and $w(d_0,d)$ for the relative weight. Let $\mathcal B$ consist of terms whose associated lattice contains a vector in the $E$-span of the designated frame family but outside its integral span. Put $$A_d(U)=\sum_{t\in\mathcal T_d\cap U}\mu(t)\omega(t),\quad S(U)=\sum_{d\in\mathcal D}\max(w(d_0,d),0)|A_d(U)|^2,$$ $$M=\sum_{d\in\mathcal D}\max(w(d_0,d),0)\sum_{t\in\mathcal T_d}\max(\mu(t),0).$$ With the source's local determinant factor $H_P$, residue cardinality $q_F$, and extended nonnegative sums, $$S(\mathcal B)\le H_P^{C(r+1)^2}q_F^{-(k-2r-5)}M,\qquad S(\mathcal B^c)\le H_P^{C(r+1)^2}M,\qquad S(\mathcal T)\le H_P^{C(r+1)^2}M.$$ If the model is nonsplit and the relative Gram determinant and all endpoint minors are integral units, then $H_P=1$ and $S(\mathcal B^c)=S(\mathcal T)=M$.

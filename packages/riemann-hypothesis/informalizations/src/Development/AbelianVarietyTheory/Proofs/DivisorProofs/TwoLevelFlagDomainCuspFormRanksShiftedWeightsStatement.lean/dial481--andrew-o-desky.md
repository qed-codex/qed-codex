---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/TwoLevelFlagDomainCuspFormRanksShiftedWeightsStatement.lean",
  "declarations": [
    "GlobalTheory.T.twoLevelFlagDomain_cuspForm_ranks_shifted_weights"
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

## Dimensions of cusp spaces at shifted weights

[Theorem AGR.1406](https://andrewodesky.com/rh/lean/GlobalTheory.T.twoLevelFlagDomain_cuspForm_ranks_shifted_weights/)

Let $E$ be a CM number field, $r\ge0$, $U$ a finite group acting on a finite set $C$, and let $M$ be the source's two-level flag-domain data. Thus the components indexed by $C$ have common Hermitian form, CM embeddings $\Psi$, signature break $p$, and compatible lattice-preserving transition maps for $U$. Assume $0<p<r$ and the source's level condition after restricting $U$ to its identity subgroup. Put $$d_X=|\Psi|p(r-p),\qquad d_Y=|\Psi|r(r-1)/2,\qquad s=2r+50r^2d_X+2.$$ Fix a weight $\kappa$ and an integer $T\ge s$. Assume the source's archimedean section package for $(M,\kappa,T)$: there are weights $L,F$ with $\kappa=F+TL$, adjacent gaps of $L$ within each signature block at least $1$, and last-minus-first entry at least $1.9T$; the weight $F-k_{\log}-(d_Y+2)L$ has within-block gaps at least zero and last-minus-first entry at least $1$. Here $(k_{\log})_{\tau,i}=2i-(r-1)$, with indices starting at zero. At every component the package also requires the prescribed archimedean model with its quantitative Levi-form margins and flat-section data.

Set $\delta_{\tau,i}=-s/2$ for $i<p$ and $\delta_{\tau,i}=s/2$ for $i\ge p$. The spaces $S_\kappa,S_{\kappa+2\delta},S_{\kappa-\delta}$, defined as spans of the componentwise cusp forms restricted to the flag domain, are all finite-dimensional, and $$\left(1-\frac{d_Y(d_Y+6)}T\right)\dim S_\kappa\le\dim S_{\kappa-\delta},\qquad\dim S_{\kappa+2\delta}\le2\dim S_{\kappa-\delta}.$$

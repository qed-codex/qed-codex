---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/CubicalLineBundles/ExistsTensorDecompositionPureTypeCmTripleStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_tensor_decomposition_pure_type_cm_triple"
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

## A tensor decomposition of a polarized abelian scheme of pure CM type

[Theorem AV.0817](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_tensor_decomposition_pure_type_cm_triple/)

Assume ([Theta functions for a principally polarized complex abelian variety](https://andrewodesky.com/rh/lean/GlobalTheory.thetaUnifAV_closed/)), the polarized abelian-scheme laws listed in the conventions, and ([Extension of semiabelian homomorphisms over a discrete valuation ring](https://andrewodesky.com/rh/lean/GlobalTheory.HomExtExamples.homExtendsOverDVR_holds/)). Fix a CM field datum $H$ with CM field $E$, quadratic-order generator $w_0$ and element $\varrho=2w_0-1$. Let $k\subset\mathbb C$ be a number field, $\omega\in\mathcal O_k$, and $C/\mathcal O_k$ an elliptic object of this datum with tangent eigenvalue $\omega$. Let $T/\mathcal O_k$ be a polarized abelian scheme with the datum's cubical structure and $\mathcal O_E$-action. Assume $C$ has a principal quadratic period lattice at the inclusion $k\hookrightarrow\mathbb C$, and $T$ has pure type $(r,0)$ relative to $2\omega-1$.

There exist a number field $k\subseteq k_1\subset\mathbb C$, $\omega_1\in\mathcal O_{k_1}$ and objects $C_1,T_1$ over $\mathcal O_{k_1}$ extending $C,T$ with their specified structures. There also exist a polarized lattice datum $(\Lambda,E_\Lambda,p,q)$ for $H$, a unit $\epsilon\in\mathbb Z^\times$ and a map $h:\Lambda\times\Lambda\to\mathbb Z[w_0]$ such that $p+q=r$, $$h(x,y)=\epsilon\bigl(E_\Lambda(w_0x,y)-E_\Lambda(x,y)\bigr)+\epsilon E_\Lambda(x,y)w_0,$$ $$\epsilon E_\Lambda(w_0x,x)>0\qquad(x\ne0),$$ and $T_1$ is the Serre tensor product $\Lambda\otimes_{\mathbb Z[w_0]}C_1$, equivariantly for the $\mathcal O_E$-action. Its polarization biextension, restricted along the tensor inclusions indexed by $a,b\in\Lambda$, agrees with the biextension of $C_1$ after applying its endomorphism $h(a,b)$ in the first variable.

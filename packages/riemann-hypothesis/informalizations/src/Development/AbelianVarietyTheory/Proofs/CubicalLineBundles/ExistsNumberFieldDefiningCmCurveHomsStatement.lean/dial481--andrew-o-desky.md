---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/CubicalLineBundles/ExistsNumberFieldDefiningCmCurveHomsStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_numberField_defining_cm_curve_homs"
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

## A number field defining prescribed CM elliptic homomorphisms

[Theorem AV.0632](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_numberField_defining_cm_curve_homs/)

Assume ([Theta functions for a principally polarized complex abelian variety](https://andrewodesky.com/rh/lean/GlobalTheory.thetaUnifAV_closed/)) and the polarized base-change assertion stated in the conventions. Let $K$ be a quadratic number field with a nonreal embedding $\sigma:K\hookrightarrow\mathbb C$, and assign a nonzero integral ideal $\mathfrak b_C\subseteq\mathcal O_K$ to each $C\in\operatorname{Cl}(\mathcal O_K)$.

Suppose there are initial data of the following kind over some number field $M\subseteq\mathbb C$ containing $\sigma(K)$: polarized elliptic schemes $P,Q_C$ over $\mathcal O_M$, tangent vectors $v,t_C$ that are bases and remain bases after every polarized base change, period lattices $\Lambda_{0,s},\Lambda_{C,s}\subseteq\mathbb C$ for every $s:\mathcal O_M\to\mathbb C$, and units $\delta_C\in\mathcal O_M^\times$. The lattices are those obtained by using the transported tangent vectors as the uniformizing coordinate. Require $$\Delta(\Lambda_{C,s})=s(\delta_C),\qquad\Lambda_{0,s_0}=c\sigma(\mathcal O_K)\quad(c\in\mathbb C^\times),$$ where $s_0$ is the inclusion. Suppose also there are $\beta_C\in\mathbb C^\times$ such that $$\beta_C\sigma(x)\Lambda_{0,s_0}\subseteq\Lambda_{C,s_0}\quad(x\mathfrak b_C\subseteq\mathcal O_K),$$ $$\beta_C^{-1}\sigma(y)\Lambda_{C,s_0}\subseteq\Lambda_{0,s_0}\quad(y\in\mathfrak b_C).$$

Then such data can be chosen over a number field $M\subseteq\mathbb C$ with an embedding $\kappa:K\hookrightarrow M$ extending $\sigma$, and with $\beta_C\in M^\times$, so that the following homomorphisms of the generic elliptic fibres exist: $$P_M\to P_M\quad\text{with tangent multiplier }\kappa(a)\quad(a\in\mathcal O_K),$$ $$P_M\to(Q_C)_M\quad\text{with tangent multiplier }\beta_C\kappa(x)\quad(x\mathfrak b_C\subseteq\mathcal O_K),$$ $$(Q_C)_M\to P_M\quad\text{with tangent multiplier }\beta_C^{-1}\kappa(y)\quad(y\in\mathfrak b_C).$$ These assertions hold for any chosen polarized models of the generic fibres and the transported tangent bases.

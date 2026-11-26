---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/CrystallineSummandAndDualFromInverseCharacterTwiStatement.lean",
  "declarations": [
    "GlobalTheory.T.crystalline_summand_and_dual_from_inverse_character_twist"
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

## Crystalline summands and filtration jumps after a character twist

[Theorem PHT.0911](https://andrewodesky.com/rh/lean/GlobalTheory.T.crystalline_summand_and_dual_from_inverse_character_twist/)

Fix the source's global arithmetic datum, an index $i$ of its local coefficient data, and a place $w\mid\ell_i$ of its CM field $E$. Assume its crystalline, de Rham and integral period data at $\ell_i$ are compatibly identified with Fontaine's rings. Let $L'$ be any finite coefficient extension containing the prescribed coefficient field at $(i,w)$. Let $r_x,\rho_x$, indexed by the specified set $X_i$, be representations of $G_E$ on $O_i^{n}$ and $O_i^{r}$, respectively, where $O_i$ is the prescribed coefficient ring. Fix $\pi\in X_i$ and suppose over $\operatorname{Frac}(O_i)$ that $$r_\pi\simeq\rho_\pi\oplus\bigoplus_{j=1}^t\chi_j,$$ with the datum's characters. Restrict to $G_{E_w}$, extend coefficients to $L'$, and put $$R=r_\pi\otimes\chi_1^{-1},\qquad W=\rho_\pi\otimes\chi_1^{-1},\qquad T=W^\vee\otimes\epsilon,$$ where $\epsilon$ is the cyclotomic character. If $R$ is crystalline, then $W,T$ are crystalline. If $R$ is de Rham, then $W,T$ are de Rham. For every embedding $\tau:E_w\hookrightarrow L'$ and $a\in\mathbb Z$, $$m_W(\tau,a)=m_R(\tau,a)-1_{\{0\le a<t\}},\qquad m_T(\tau,a)=m_W(\tau,-a-1).$$

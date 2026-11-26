---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ImportsTailTer.lean",
  "declarations": [
    "GlobalTheory.StrongApproxSUProof.strongApproxSU"
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

## Strong approximation for special unitary groups

[Theorem AGR.0058](https://andrewodesky.com/rh/lean/GlobalTheory.StrongApproxSUProof.strongApproxSU/)

Let $E/F$ be a CM extension of number fields with conjugation $\sigma$. Let $M\in\mathbb N$ with $M\ge2$, and let $J\in\operatorname{Mat}_M(E)$ satisfy $\sigma(J)^{\mathsf T}=J$ and $\det J\ne0$.

Write $\mathbb A_F$ for the adele ring of $F$, put $B=\mathbb A_F\otimes_F E$, and let the bar on $B$ denote $1\otimes\sigma$. Let $J_B$ be the image of $J$ in $\operatorname{Mat}_M(B)$. Define $$U(\mathbb A_F)=\{u\in\operatorname{GL}_M(B):\overline u^{\mathsf T}J_Bu=J_B\},\qquad G(\mathbb A_F)=\{u\in U(\mathbb A_F):\det u=1\}.$$ Likewise put $U(F)=\{q\in\operatorname{GL}_M(E):\sigma(q)^{\mathsf T}Jq=J\}$. The map $\iota$ sends a matrix over $E$ to the matrix obtained by applying $a\mapsto1\otimes a$ to each entry. Define the rational subgroup $$G(F)=G(\mathbb A_F)\cap\iota(U(F)).$$

Choose finite sets $S_\infty$ of infinite places and $S_f$ of finite places of $F$. Let $\epsilon\in\mathbb A_F$ have component $1$ at every selected place and component $0$ at every other place, and put $\epsilon_B=\epsilon\otimes1\in B$. Define $$G_S=\{g\in G(\mathbb A_F):\epsilon_B(g-I_M)=g-I_M\},$$ where $I_M$ is the identity matrix and the equality is entrywise. If $G_S$ is not compact, then $$G(\mathbb A_F)\subseteq\overline{\{\gamma h:\gamma\in G(F),\ h\in G_S\}}^{\,U(\mathbb A_F)}.$$

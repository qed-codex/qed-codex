---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/PolynomialProperness/IsoRightInv.lean",
  "declarations": [
    "PI.PolynomialProperness.isoCore"
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

## Bounding an isometry by its values on a nondegenerate subspace

[Theorem REP.0809](https://andrewodesky.com/rh/lean/PI.PolynomialProperness.isoCore/)

Let $H\in M_n(\mathbb C)$ satisfy $H^*=H$ and $H^2=1$, and put $h(x,y)=\overline y^{t}Hx$. Let $(m_i)_{i\in I}$ be a finite family in $\mathbb C^n$ with nonsingular Gram matrix $(h(m_j,m_i))_{i,j}$. Suppose $$h(x,m_i)=0\ (i\in I)\quad\Longrightarrow\quad \operatorname{Re}h(x,x)\ge0.$$ There is a real constant $C$ such that for every $s\in M_n(\mathbb C)$ with $s^*Hs=H$ and every $K\ge0$, $$\bigl(\|sm_i\|_2^2\le K\text{ for all }i\bigr)\quad\Longrightarrow\quad \|sx\|_2^2\le C(1+K)^2\|x\|_2^2\quad(x\in\mathbb C^n).$$

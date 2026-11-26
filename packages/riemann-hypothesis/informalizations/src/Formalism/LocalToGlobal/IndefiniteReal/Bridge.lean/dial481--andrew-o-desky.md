---
{
  "module": "src/Formalism/LocalToGlobal/IndefiniteReal/Bridge.lean",
  "declarations": [
    "Formalism.IndefR.Bridge.ActTie",
    "Formalism.IndefR.Bridge.ClassPres",
    "Formalism.IndefR.Bridge.FamReal",
    "Formalism.IndefR.Bridge.HeckeTie"
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

## Rational class presentations and Hecke comparison

[Definition / hypothesis ARAK.D159](https://andrewodesky.com/rh/lean/Formalism.IndefR.Bridge.FamReal/)

Hypothesis (rational class presentations). Use a rational coefficient datum and its form space from ([Class sums and finite Hecke families](https://andrewodesky.com/rh/lean/Formalism.L2.DIV.CSD/)), over the number field $K$ with distinguished embedding $\jmath:K\hookrightarrow\mathbb C$. Thus its finite class set is $C$, its coefficient space is $V_K$ with designated basis $(b_a)$ and Hermitian pairing $B$, and each class has a finite stabilizer $\Gamma_c$ acting on $V_K$. The data also include the two specified integral coefficient lattices $N_c,D_c$. Fix groups $\Gamma,H$, a homomorphism $i:\Gamma\to H$, a complex inner-product space $W$, a representation $\rho:\Gamma\to\operatorname{End}_{\mathbb C}W$, subgroups $J\subseteq Q\subseteq H$, and characters $\chi:J\to\mathbb C^\times$, $\widetilde\chi:Q\to\mathbb C^\times$ whose restriction is $\chi$.

Choose representatives $y_c\in H$ such that every $h\in H$ belongs to $i(\Gamma)y_cJ$ for exactly one $c$. For each $c$ choose a group isomorphism $$s_c:\Gamma_c\simeq\{\gamma\in\Gamma:y_c^{-1}i(\gamma)y_c\in J\}.$$ Choose a $\jmath$-semilinear map $u:V_K\to W$ whose values $u(b_a)$ are linearly independent over $\mathbb C$ and span $W$. Require $$\langle u(v),u(v')\rangle=\jmath(B(v,v')),$$ $$u(\rho_c(a)v)=\chi\bigl((y_c^{-1}i(s_c(a))y_c)^{-1}\bigr)\,\rho(s_c(a))u(v).$$ For a rational form $f:C\to V_K$, choose once a decomposition $h=i(\gamma_h)y_{c_h}k_h$, $k_h\in J$, and define its extension by $$\mathcal E(f)(h)=\chi(k_h)\rho(\gamma_h)u(f(c_h)).$$ These choices of decomposition are fixed in this construction.

The finite-group comparison requires a surjective homomorphism $r_Q:Q\to G$ with $$r_Q(q)=1\quad\Longleftrightarrow\quad q\in J.$$ For every $g\in G$, every lift $q\in Q$ with $r_Q(q)=g$, and every rational form, require $$\mathcal E(gf)(h)=\widetilde\chi(q)^{-1}\mathcal E(f)(hq).$$

For an operator family $T_a$ with specified admissible indices, choose $x_a\in H$ and a finite set $A_a\subset H$ for every index. At every admissible index require: $x_a$ has the specified Hecke type; every member of $A_a$ has the specified local support; $\chi(k)=1$ for every $k\in J$ having that local support; and $A_a\subset Jx_aJ$, with every $h\in Jx_aJ$ belonging to $aJ$ for exactly one $a\in A_a$. Require the exact identity $$\mathcal E(T_af)(h)=\sum_{z\in A_a}\mathcal E(f)(hz).$$ The choices $x_a,A_a$ exist at all indices; these conditions apply only in the specified admissible range.

Apply these constructions to every right and lifted rational form space in ([Class sums and finite Hecke families](https://andrewodesky.com/rh/lean/Formalism.L2.DIV.CSD/)). For a Hermitian space $U$ in ([Analytic and rational realization data](https://andrewodesky.com/rh/lean/Formalism.IndefR.Links.RealDat/)), take $H$ to be the finite-component image of $U(U)(\mathbb A_F)$, $\Gamma=U(U)(F)$, and $i$ its finite-component homomorphism. Take $W$ and $\rho$ to be the chosen coefficient space and the restriction of its adelic representation. Take $J,Q$ and their characters to be the finite levels defined in ([Finite levels and character matching](https://andrewodesky.com/rh/lean/Formalism.IndefR.Links.LevCh.Is/)). Require all the class, finite-group and Hecke comparisons above on the right space $X'$ and on every input space $V_{i+1}$, for every tuple. For split Hecke operators of degree $a$ the admissible range is $1\le a\le\dim_E U$. The right rank is $r+mt$, and every input rank is $r+t$.

---
{
  "module": "src/Formalism/LocalToGlobal/HermitianForms/TiedTwSymP.lean",
  "declarations": [
    "Formalism.L2.Forms.SymmetricTwistedTiltedData",
    "Formalism.L2.Forms.TwPAtGS",
    "Formalism.L2.Forms.TwPEvzS",
    "Formalism.L2.Forms.TwPTiedS"
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

## Twisted terminal lattices and period values

[Definition / hypothesis ARAK.D166](https://andrewodesky.com/rh/lean/Formalism.L2.Forms.SymmetricTwistedTiltedData/)

Use ([Twisted coordinate values and local operators](https://andrewodesky.com/rh/lean/Formalism.L2.Forms.TwAtT/)) and ([Terminal column lattices and period values](https://andrewodesky.com/rh/lean/Formalism.L2.Forms.ClsPTied/)), with the same untwisted and twisted member data of ([Integral forms on column representations](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.MemberForms/)) and ([Column chains and period pairings](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Member/)). Put $n=N_m-1$. In the terminal local integral criterion a coefficient place is permitted when $\ell_w=T_u$ or $\ell_w$ belongs to none of the $F$-prime ideals in $Q_\mu$.

Hypothesis (twisted secondary values). At every source and every $\mu\ne\mu_0$, choose the entire secondary class, level, lattice, stabilizer and value presentation of ([Terminal column lattices and period values](https://andrewodesky.com/rh/lean/Formalism.L2.Forms.ClsPTied/)), with bad places $Q_\mu\cup\{v:v\mid g_0g_1\}$. Thus it includes the exact terminal weight formula, the character-equivariant finite form space, the inverse-stabilizer-weighted pairing with reversed polynomial arguments, the rational-image criterion and the embedding-dependent majorant norm identity. Its local integral criterion is imposed at every permitted coefficient place defined above.

Its base lattice is exactly the untwisted secondary base lattice. Its adelic character has finite order, with one positive exponent working for all level elements. At every $v\mid g_0g_1$ its local subgroup equals the untwisted secondary local subgroup. Its character equals the untwisted secondary character on common matrices with identity components at every place of $Q_\mu$.

Hypothesis (twisted terminal extension). For every nonbase twist choose $z_0\in E z\subset E^{N_m}$ with $h(z_0,z_0)=T_u$. For each twisted secondary class choose $\gamma_c\in U(X_m)(F)$ and $\kappa_c$ in the coordinate terminal level of the branch containing $\operatorname{til}(c)$. Require $$\gamma_cL_{m,\operatorname{til}(c)}=i(M_c)+\mathcal O_Ez_0.$$ For every terminal dual vector $x$ and $a\in\mathcal O_E$ with $a=h(z_0,\gamma_cx)$, its prescribed finite functional is $r_v(a)$. If $s$ belongs to a secondary stabilizer, its prescribed image in the terminal stabilizer, conjugated by $\gamma_c$, restricts on $i(X')$ to the secondary stabilizer matrix and fixes $z_0$. For every finite adelic matrix $g$ satisfying $gi=iy_c$ and $gz_0=z_0$, require $$\gamma_cy_{\operatorname{til}(c)}=g\kappa_c.$$

Hypothesis (twisted evaluation and periods). At every twist, including $\mu_0$, choose a complex linear equivalence $e_{W_z}$ from its recorded $W_z$ to functions on its secondary classes and terminal values, and a conjugate-linear map $j_M$ from its period input to row functions. For every $\mu\ne\mu_0$, every $\varphi,c,s,s'$ with $eY(s)=\gamma_{c,\infty}eY(s')$, require $$e_{W_z}(\operatorname{evz}\varphi)(c,s)=\chi_m(\kappa_c)^{-1}\varphi(\operatorname{til}(c),s').$$ For every nonbase twist the image of $j_M$ is exactly the secondary finite form space and $$\operatorname{period}(w,F)=\operatorname{ipP}(j_MF,w)$$ for every $w,F$. The chosen maps at $\mu_0$ are part of the data; these last two identities are required here only at the nonbase twists.

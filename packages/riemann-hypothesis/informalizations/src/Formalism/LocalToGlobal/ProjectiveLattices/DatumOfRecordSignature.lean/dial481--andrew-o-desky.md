---
{
  "module": "src/Formalism/LocalToGlobal/ProjectiveLattices/DatumOfRecordSignature.lean",
  "declarations": [
    "Formalism.L2.Pj.datumOfRecord"
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

## Canonical integral modules for original moduli

[Definition / hypothesis ARAK.D195](https://andrewodesky.com/rh/lean/Formalism.L2.Pj.LawsM.pins/)

Hypothesis (canonical original moduli). Use the arithmetic and Hermitian member data of ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)), with CM extension $E/F$, quadratic subfield $E_0=\mathbb Q(s_d)$, chosen embedding $\phi_0:E\hookrightarrow\mathbb C$, generator primes $g_0,g_1$, reference Hermitian lattices $(W_j,h_j,L_{0,j})$, coefficient ring $O\to K$, and conjugation denoted by a bar. Use the ideal $\mathfrak c\subset\mathcal O_{E_0}$ and different factor $\mathfrak b_0$ in ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)). Put $$\mathfrak a=(\mathfrak c\mathcal O_E)\mathfrak b_0^{-1},\qquad\xi_0=-\frac1{N\mathfrak c\,s_d}.$$ The geometric host of the original moduli family in ([Polarized modules and unitary moduli](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.Tor.Host/)) is exactly $$d_{\rm mod}=d,\quad\rho=s_d,\quad w=(1+s_d)/2,\quad\rho_\infty=\phi_0(s_d),$$ with CM conjugation on $\mathcal O_E$. Every selected arithmetic CM embedding takes $s_d$ to $\phi_0(s_d)$.

The original level has $M=g_0g_1$ and $A=1$. Its coefficient number field $K_0\subset\mathbb C$ contains every image of $E$ and the chosen primitive $M$th root. There is a ring isomorphism $\mathcal O_{K_0}\simeq O$ whose composite into $K\hookrightarrow\mathbb C$ is the natural inclusion. Choose primes $\mathfrak p_i\subset\mathcal O_{E_0}$ above $g_i$ for $i=0,1$ and take the original level ideal to be $$\mathfrak b=(\mathfrak p_0\mathcal O_E)(\mathfrak p_1\mathcal O_E).$$ The complete original-level and coefficient-field meanings are the ones in ([Polarized modules and unitary moduli](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.Tor.Host/)) and ([Coefficient fields and deeper moduli levels](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.Tor.Level/)).

Require the following universal fractional-ideal identity: for every arithmetic field and Galois datum satisfying ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)), with its own $\xi_0,\mathfrak a$ and absolute different $\mathfrak D_{E/\mathbb Q}$, $$(\xi_0)\mathfrak a\bar{\mathfrak a}\,\mathfrak D_{E/\mathbb Q}=\mathcal O_E.$$ For the present member and every selected stage $1\le j\le m$, put $$\Lambda_j^{\rm can}=\operatorname{span}_{\mathcal O_E}\{av:a\in\mathfrak a,\ v\in L_{0,j}\},\qquad B_j(x,y)=\operatorname{Tr}_{E/\mathbb Q}\{\xi_0h_j(x,y)\}.$$ The trace is integral on $\Lambda_j^{\rm can}$. Define $\epsilon_j=1$ if the unsigned integer form $B_j$ admits the complex structure and trace identities in the next paragraph, and $\epsilon_j=-1$ otherwise. Take the original integral polarized module itself to be $\Lambda_j^{\rm can}$, with signature $$p_j=k+j-1,\qquad q_j=m-j,$$ and alternating form $E_j=\epsilon_jB_j$.

Here the complex-structure condition for an integer form $E$ on this module means that there is a real-linear $J$ on $\mathbb R\otimes_\mathbb Z\Lambda_j^{\rm can}$ with $J^2=-1$, $E(Jx,Jy)=E(x,y)$ and $E(Jx,x)>0$ for $x\ne0$. It commutes with every $a\in\mathcal O_E$. For the action $A_a$ of $a$, require $$\operatorname{tr}_{\mathbb R}A_a=2\Re T_j(a),\qquad\operatorname{tr}_{\mathbb R}(JA_a)=-2\Im T_j(a),\qquad T_j(a)=\sum_{\tau\in\Sigma}\{p_j\tau(a)+q_j\bar\tau(a)\}.$$ The chosen signed form $E_j$ satisfies this condition and is unimodular, and $\operatorname{rank}_{\mathcal O_E}\Lambda_j^{\rm can}=p_j+q_j$. These are the integral-module and positivity conditions in ([Polarized modules and unitary moduli](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.Tor.Host/)) for this exact lattice and signed form.

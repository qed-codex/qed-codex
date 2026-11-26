---
{
  "module": "src/Formalism/LocalToGlobal/ProjectiveLattices/RecCond.lean",
  "declarations": [
    "Formalism.L2.Pj.OKPsi"
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

## Ideal generators in rational moduli realizations

[Definition / hypothesis ARAK.D142](https://andrewodesky.com/rh/lean/Formalism.L2.Pj.OKPsi/)

Hypothesis (ideal generators in rational moduli realizations). Fix the arithmetic and Hermitian member data in ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)). Let $E/F$ be its CM extension, $E_0=\mathbb Q(s_d)$ its distinguished quadratic field, $\phi_0:E\hookrightarrow\mathbb C$ its chosen embedding and $K\hookrightarrow\mathbb C$ its coefficient field. Write $O\to K$ for the homomorphism from its coefficient ring and $\Sigma$ for its CM type. Use the ideal $\mathfrak c\subset\mathcal O_{E_0}$ and different factor $\mathfrak b_0$ of ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)), and put $$\mathfrak a=(\mathfrak c\mathcal O_E)\mathfrak b_0^{-1},\qquad \xi_0=-1/(N\mathfrak c\,s_d).$$

The condition below is universal over the following original rational moduli data. Choose a geometric host and, at every natural stage, an integral polarized module and moduli scheme in the sense of ([Polarized modules and unitary moduli](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.Tor.Host/)), all with a common original level. Require the geometric host's prime, integral square root and complex square root to be respectively $d,s_d,\phi_0(s_d)$, and require every selected CM embedding to carry $s_d$ to this same complex square root. Set $w=(1+s_d)/2$. The original level has odd $M=g_0g_1\ge3$, auxiliary level $A=1$, and an ideal $\mathfrak b\subset\mathcal O_E$ such that $$\mathfrak b\bar{\mathfrak b}=(M),\qquad\mathfrak b+\bar{\mathfrak b}=\mathcal O_E,\qquad\mathfrak b=\operatorname{span}_{\mathcal O_E}(\mathfrak b\cap\mathbb Z[w]).$$ Choose a number field $F_*\subset\mathbb C$ containing every complex image of $E$, $\phi_0(s_d)$ and $\exp(2\pi\mathrm i/M)$. It comes with an isomorphism $\mathcal O_{F_*}\simeq O$ such that the composite into $K\hookrightarrow\mathbb C$ is the natural inclusion of $\mathcal O_{F_*}$.

At each stage $1\le j\le m$, the integral module $\Lambda_j$ has signature $$p_j=k+j-1,\qquad q_j=m-j.$$ There is an $\mathcal O_E$-linear injection $\iota_j:\Lambda_j\to W_j$, where $W_j$ is the member's stage-$j$ Hermitian space with its reference lattice $L_{0,j}$, and a sign $\epsilon_j\in\{1,-1\}$ such that $$\iota_j(\Lambda_j)=\operatorname{span}_{\mathcal O_E}\{av:a\in\mathfrak a,\ v\in L_{0,j}\},\qquad E_{\Lambda_j}(x,y)=\epsilon_j\operatorname{Tr}_{E/\mathbb Q}\{\xi_0h_{W_j}(\iota_jx,\iota_jy)\}.$$

For every such realization, every $1\le j\le m$ and every nonzero ideal $\mathfrak d\subset\mathcal O_E$, require an element $\beta\in F_*^\times$ satisfying $$\beta\mathcal O_{F_*}=\prod_{\rho:E\hookrightarrow\mathbb C}(\rho(\mathfrak d)\mathcal O_{F_*})^{d_{j,\rho}},\qquad |\sigma(\beta)|^2=(N\mathfrak d)^{p_j+q_j}\quad(\sigma:F_*\hookrightarrow\mathbb C),$$ where $d_{j,\rho}=p_j$ for $\rho\in\Sigma$ and $d_{j,\rho}=q_j$ for $\rho\notin\Sigma$. Every image $\rho(E)$ is contained in $F_*$ by its coefficient-field conditions.

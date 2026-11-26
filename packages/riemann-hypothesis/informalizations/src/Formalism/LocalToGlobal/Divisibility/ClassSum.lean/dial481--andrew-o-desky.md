---
{
  "module": "src/Formalism/LocalToGlobal/Divisibility/ClassSum.lean",
  "declarations": [
    "Formalism.L2.DIV.CSD"
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

## Class sums and finite Hecke families

[Definition / hypothesis ARAK.D202](https://andrewodesky.com/rh/lean/Formalism.L2.DIV.CSD/)

Hypothesis (class sums). Let $K$ be a number field with involution, and let $$K_{\rm c}=\{a\in K:\sigma(\bar a)=\overline{\sigma(a)}\text{ for every }\sigma:K\hookrightarrow\mathbb C\}.$$ A class-sum datum consists of a finite set $C$, a finite-dimensional $K$-vector space $V$ with its restricted $\mathcal O_K$-module structure and a specified finite basis, a sesquilinear pairing $b:V\times V\to K$ conjugate-linear in its first variable, and, for each $c\in C$, a finite group $\Gamma_c$, a representation $\rho_c:\Gamma_c\to\operatorname{End}_K(V)$ and two $\mathcal O_K$-submodules $N_c,D_c\subset V$. Its space of forms and weighted pairing are $$\mathcal F=\{f:C\to V:\rho_c(\gamma)f(c)=f(c)\text{ for all }c,\gamma\},\qquad (f,g)=\sum_{c\in C}\frac{b(f(c),g(c))}{|\Gamma_c|}.$$ Fix a basis of $\mathcal F$ whose values have coordinates in $K_{\rm c}$ whenever such a basis exists; otherwise fix an arbitrary basis. Denote its coordinate evaluation map by $I:K^{\dim\mathcal F}\to(C\to V)$ and the Gram matrix of the displayed pairing by $H$. The two coordinate integral modules are $\{x:I(x)(c)\in N_c\ \forall c\}$ and $\{x:I(x)(c)\in D_c\ \forall c\}$. No positivity, symmetry or lattice condition is included in the definition of these data.

**Rational families.** Fix a finite group $G$, sets $\mathcal P,\mathcal I,\mathcal A,\mathcal T$, and a finite set $J$. A block datum $B$ over $\mathcal P$ consists of a class-sum datum with form space $\mathcal F$, a $K$-linear representation $\rho$ of $G$ on $\mathcal F$, a set $\mathcal P_B$ with a map $p_B:\mathcal P_B\to\mathcal P$, natural numbers $n_B,t_B$, a function $q_B:\mathcal P_B\to\mathbb N$, endomorphisms $T^B_{P,d}$ of $\mathcal F$ for $P\in\mathcal P_B,d\in\mathbb N$, and a finite list of functions $\nu_{B,s}:\mathcal P_B\to K$. Additional inert data consist of a set $\mathcal I_B$, a map $i_B:\mathcal I_B\to\mathcal I$ and endomorphisms $U^B_{P,a}$ of $\mathcal F$ for $P\in\mathcal I_B,a\in\mathcal A$.

A rational family consists of an infinite place $v_0$ of $K$, a base tuple $t_0\in\mathcal T$, a finite set $\mathcal X\subset K^G$, a right block datum $B^R_t$ for every $t\in\mathcal T$, a lifted block datum $B^L_{j,t}$ for every $j\in J,t\in\mathcal T$, inert data on each of these block data, and maps $$\tau_j:(\mathcal P\to K[X])\longrightarrow(\mathcal P\to K[X]),\qquad \tau_j^I:(\mathcal I\times\mathcal A\to K)\longrightarrow(\mathcal I\times\mathcal A\to K).$$ Write $R_t$ and $L_{j,t}$ for the right and lifted form spaces. A full spectral label is a pair $(S,u)$ of a function $S:\mathcal P\to K[X]$ and a function $u:\mathcal I\times\mathcal A\to K$; its transfer at $j$ is $(\tau_j(S),\tau_j^I(u))$.

**Finite Hecke families.** A particular class of rational families has $J=\{0,\ldots,m-1\}$ for a natural number $m$, and $\mathcal A=\mathbb N^{<\omega}$ is the set of finite sequences of natural numbers. Choose natural numbers $r_A,t_A$, natural numbers $q_P$ for $P\in\mathcal P$, units $\mu_{j,t,P},\eta_P\in K^\times$, and subsets $\mathcal P_t\subset\mathcal P$, $\mathcal I_t\subset\mathcal I$. For the right and lifted block data at $t$, take $\mathcal P_B=\mathcal P_t$, $\mathcal I_B=\mathcal I_t$, both place maps to be inclusions, and $q_B(P)=q_P$. Use the degrees, block lists and polynomial transfer specified below; choose the class-sum data, representations, endomorphisms and inert transfer maps arbitrarily.

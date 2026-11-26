---
{
  "module": "src/Development/AbelianVarietyTheory/Definitions/Degenerations/RigGen.lean",
  "declarations": [
    "GlobalTheory.ZH.HypS",
    "GlobalTheory.ZH.ThetaSys.Real"
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

## Theta systems, their realizations on abelian schemes, and rational models

[Definition / hypothesis AV.D264](https://andrewodesky.com/rh/lean/GlobalTheory.ZH.ThetaSys/)

Throughout, $o$ is a commutative ring and $\Omega$ is a field with an $o$-algebra structure.

**Theta systems.** A *theta system* over $(o,\Omega)$ consists of the following.

- Integers $g\ge0$, $N\ge2$ and $r\ge1$ such that $rN$ is a unit of $o$, and an element $\zeta\in o$ of multiplicative order exactly $(rN)^2$. Put $$\Gamma=(\mathbb Z/rN\mathbb Z)^{2g},\qquad e(a,b)=\sum_{i=1}^g\bigl(a_ib_{g+i}-a_{g+i}b_i\bigr)\in\mathbb Z/rN\mathbb Z\quad(a,b\in\Gamma).$$
- A finite nonempty set $J$ and matrices $\rho(a)\in M_J(o)$ for $a\in\Gamma$. They satisfy $\rho(a)=1$ whenever $ra=0$; for all $a,b$ there is an integer $k\ge0$ with $\rho(a)\rho(b)=\zeta^k\rho(a+b)$; and $\rho(a)\rho(b)=\rho(a+b)$ whenever $r\,e(a,b)=0$.
- A finitely generated $o$-subalgebra $R\subseteq\Omega$ whose field of fractions is $\Omega$.
- Elements $\theta(a)\in R$ for $a\in\Gamma$, called the *theta constants*, and elements $\varepsilon(a,i)\in R$ for $a\in\Gamma$ and $i\in J$. At least one $\theta(a)$ is nonzero, and the elements $a$ with $\theta(a)\ne0$ generate the group $\Gamma$.

**Realizations.** Let $\mathcal S=(g,N,r,\zeta,J,\rho,R,\theta,\varepsilon)$ be a theta system. A *polarized abelian scheme* over a scheme $T$ is an abelian scheme $E\to T$, in the sense of ([Abelian and semiabelian group schemes](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Semi.IsAbelianScheme/)), smooth of some relative dimension, with a line bundle $\mathcal L$ on $E$ that admits a rigidification, is locally symmetric over $T$ and has trivial translation kernel, in the senses of ([Rigidification, symmetry and translation kernels](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Out.Rigidified/)), and is relatively ample in the sense of ([Relative ampleness by affine section charts](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Out.RelAmple/)).

A *realization* of $\mathcal S$ consists of a polarized abelian scheme $(E,\mathcal L)$ over $\operatorname{Spec}R$ of relative dimension $g$ and the data (1)–(7) below. For points or homomorphisms $f,h$ with values in $E$, write $$\Delta_{\mathcal L}(f,h)=(f+h)^*\mathcal L\otimes f^*\mathcal L^{-1}\otimes h^*\mathcal L^{-1}\otimes 0^*\mathcal L,$$ and write $t_x$ for translation by a point $x\in E(R)$.

1. **Endomorphisms.** Group endomorphisms $w,w'$ of $E$ with $w+w'=\operatorname{id}_E$, such that $$\mathcal L\simeq\Delta_{\mathcal L}(\operatorname{id}_E,w)\ \text{ on }E,\qquad \Delta_{\mathcal L}(w\circ p_1,p_2)\simeq\Delta_{\mathcal L}(p_1,w'\circ p_2)\ \text{ on }E\times_RE,$$ where $p_1,p_2$ are the two projections.
2. **Exponents.** An odd prime $\ell$ and integers $k\ge2$ and $j\ge1$ with $$N=\ell^{2k},\qquad r=\ell^{j},\qquad |J|=N^g.$$
3. **Level structure.** An additive map $x:\Gamma\to E(R)$. For every algebraically closed field $K$ and every point $\operatorname{Spec}K\to\operatorname{Spec}R$, each point of $E(K)$ killed by $rN$ is the specialization of $x(a)$ for exactly one $a\in\Gamma$. For all $a,b\in\Gamma$, $$e_{\mathcal L,rN}\bigl(x(a),x(b)\bigr)=\bigl(\zeta^{rN}\bigr)^{e(a,b)},$$ with the commutator convention stated below.
4. **Theta section and frames.** A generator $\eta$ of $0^*\mathcal L$, and a section $\vartheta\in\Gamma(E,\mathcal L)$ such that every section of $\mathcal L$ is $c\vartheta$ for a unique $c\in R$. For every $a\in\Gamma$, a generator $f_a$ of the line bundle $x(a)^*\mathcal L$ on $\operatorname{Spec}R$ with the following normalization: there is an isomorphism $\alpha:[rN]^*\mathcal L\simeq\mathcal L^{\otimes(rN)^2}$ whose pullback along the zero section sends $\eta$ to $\eta^{\otimes(rN)^2}$, and $$f_a^{\otimes(rN)^2}=\bigl(x(a)^*\alpha\bigr)(\eta)$$ under the equality $x(a)^*[rN]^*\mathcal L=0^*\mathcal L$. The theta constants are the values of $\vartheta$ in these frames: $$x(a)^*\vartheta=\theta(a)\,f_a\qquad(a\in\Gamma).$$
5. **Sections of the $N$th power.** Sections $s_i\in\Gamma(E,\mathcal L^{\otimes N})$ for $i\in J$ that form a basis: every section of $\mathcal L^{\otimes N}$ is $\sum_ic_is_i$ for a unique family $(c_i)$ in $R$. Their values at the torsion points are $$x(a)^*s_i=\varepsilon(a,i)\,f_a^{\otimes N}\qquad(a\in\Gamma,\ i\in J).$$
6. **The distinguished section.** An index $i_0\in J$ and an isomorphism $\alpha_0:[\ell^k]^*\mathcal L\simeq\mathcal L^{\otimes N}$ whose pullback along the zero section sends $\eta$ to $\eta^{\otimes N}$, such that $$s_{i_0}=\alpha_0\bigl([\ell^k]^*\vartheta\bigr).$$
7. **Theta-group action.** For every $a\in\Gamma$, an isomorphism $$U(a):t_{x(ra)}^*\mathcal L^{\otimes N}\xrightarrow{\ \sim\ }\mathcal L^{\otimes N}.$$ It is symmetric of order $N$ in the sense stated below, and it acts on the basis through $\rho$: $$U(a)\bigl(t_{x(ra)}^*s_i\bigr)=\sum_{l\in J}\rho(a)_{l,i}\,s_l\qquad(i\in J).$$ For every $i\in J$ there are $a\in\Gamma$ and an integer $e\ge0$ such that the column $i_0$ of $\rho(a)$ has the entry $\zeta^e$ in row $i$ and zero in every other row.

**Arithmetic bases and rational models.** The pair $(o,\Omega)$ is an *arithmetic base* when $o$ is a Dedekind domain (a field is allowed) that is finitely generated as a ring, $\Omega$ has characteristic zero, and the structure map $o\to\Omega$ is injective.

A *rational model* of $\Omega$ over $o$ is an integral scheme $M$, separated and of finite type over $o$, with an $o$-morphism $\operatorname{Spec}\Omega\to M$ whose image is the generic point of $M$ and which identifies the function field of $M$ with $\Omega$. For $z\in M$, write $\mathcal O_{M,z}\subseteq\Omega$ for the local ring at $z$, viewed as a subring of the function field.

The theta constants of a theta system $\mathcal S$ over $(o,\Omega)$ are *divisible on* a rational model $M$ when for every $z\in M$ there is $a\in\Gamma$ with $$\theta(a)\ne0\qquad\text{and}\qquad\frac{\theta(b)}{\theta(a)}\in\mathcal O_{M,z}\ \text{ for every }b\in\Gamma.$$

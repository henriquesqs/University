package com.aplicativo.model;

import java.util.Set;

import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.JoinTable;
import javax.persistence.ManyToMany;
import javax.persistence.Table;

@Entity
@Table(name = "user")
public class User {
	
	@Id
	@GeneratedValue(strategy = GenerationType.AUTO)
	private int id;
	 
	@Column(name = "email")
	private String email;
	 
	@Column(name = "firstname")
	private String firstname; 
	 
	@Column(name = "lastname")
	private String lastname;
	 
	@Column(name = "password")
	private String password;
	
	@Column(name = "active")
	private int active;
	
	@Column(name = "fezExercicio1")
	private int fezExercicio1;
	
	@Column(name = "fezExercicio2")
	private int fezExercicio2;
	
	@Column(name = "fezExercicio3")
	private int fezExercicio3;
	 
	@ManyToMany(cascade=CascadeType.ALL)
	@JoinTable(name="user_role", joinColumns=@JoinColumn(name="user_id"), inverseJoinColumns=@JoinColumn(name="role_id"))
	private Set<Role> roles;

	public int getId() {
		return id;
	}
	
	public String getEmail() {
		return email;
	}
	
	public String getFirstname() {
		return firstname;
	}
	
	public String getLastname() {
		return lastname;
	}
	
	public String getPassword() {
		return password;
	}
	
	public int getActive() {
		return active;
	}
	
	public Set<Role> getRoles() {
		return roles;
	}
	
	public int getFezExercicio1() {
		return fezExercicio1;
	}

	public int getFezExercicio2() {
		return fezExercicio2;
	}

	public int getFezExercicio3() {
		return fezExercicio3;
	}

	public void setId(int id) {
		this.id = id;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public void setFirstname(String firstname) {
		this.firstname = firstname;
	}

	public void setLastname(String lastname) {
		this.lastname = lastname;
	}

	public void setPassword(String password) {
		this.password = password;
	}

	public void setActive(int active) {
		this.active = active;
	}

	public void setRoles(Set<Role> roles) {
		this.roles = roles;
	}
	
	public void setFezExercicio1(int fezExercicio1) {
		this.fezExercicio1 = fezExercicio1;
	}
	
	public void setFezExercicio2(int fezExercicio2) {
		this.fezExercicio2 = fezExercicio2;
	}

	public void setFezExercicio3(int fezExercicio3) {
		this.fezExercicio3 = fezExercicio3;
	}
	
}

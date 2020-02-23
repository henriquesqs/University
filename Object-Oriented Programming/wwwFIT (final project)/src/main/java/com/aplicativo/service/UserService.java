package com.aplicativo.service;

import com.aplicativo.model.User;

public interface UserService {
	
	 public User findUserByEmail(String email);
	 
	 public void saveUser(User user);
	 
	 public void addExercise1(User user);
	 
	 public void addExercise2(User user);
	 
	 public void addExercise3(User user);
	 
	 public void removeAccount(User user);
	 
	 public void changeFirstname(User user, String firstname);
	 
	 public void changeLastname(User user, String lastname);
	 
	 public void changePassword(User user, String password);
	 
	 public void changeEmail(User user, String email);

}

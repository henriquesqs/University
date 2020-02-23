package com.aplicativo.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.stereotype.Service;

import java.util.Arrays;
import java.util.HashSet;

import com.aplicativo.model.Role;
import com.aplicativo.model.User;
import com.aplicativo.repository.UserRepository;
import com.aplicativo.repository.RoleRespository;

@Service("userService")
public class UserServiceImpl implements UserService {

	@Autowired
	private UserRepository userRepository;
	 
	@Autowired
	private RoleRespository roleRespository;
	 
	@Autowired
	private BCryptPasswordEncoder bCryptPasswordEncoder;

	@Override
	public User findUserByEmail(String email) {
	  return userRepository.findByEmail(email);
	}

	@Override
	public void saveUser(User user) {
	 user.setPassword(bCryptPasswordEncoder.encode(user.getPassword()));
	 user.setActive(1);
	 Role userRole = roleRespository.findByRole("ADMIN");
	 user.setRoles(new HashSet<Role>(Arrays.asList(userRole)));
	 userRepository.save(user);
	}
	
	@Override
	public void addExercise1(User user) {
		user.setFezExercicio1(1);
		userRepository.save(user);
	}
	
	@Override
	public void addExercise2(User user) {
		user.setFezExercicio2(1);
		userRepository.save(user);
	}
	
	@Override
	public void addExercise3(User user) {
		user.setFezExercicio3(1);
		userRepository.save(user);
	}
	
	@Override
	public void removeAccount(User user) {
		user.setActive(0);
		userRepository.save(user);
	}
	
	@Override
	public void changeFirstname(User user, String firstname) {
		user.setFirstname(firstname);
		userRepository.save(user);
	}
	
	@Override
	public void changeLastname(User user, String lastname) {
		user.setLastname(lastname);
		userRepository.save(user);
	}
	
	@Override
	public void changePassword(User user, String password) {
		user.setPassword(bCryptPasswordEncoder.encode(password));
		userRepository.save(user);
	}
	
	@Override
	public void changeEmail(User user, String email) {
		user.setEmail(email);
		userRepository.save(user);
	}
}

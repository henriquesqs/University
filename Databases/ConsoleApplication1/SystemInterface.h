#pragma once

#include <iostream>
#include <stdlib.h>
#include <regex>
#include <iomanip>
#include <string>
#include "ocilib.hpp"
#include <ctype.h>

class SystemInterface {
public:
	static ocilib::Connection con;
	static ocilib::Statement st;

	static std::string name;
	static std::string cpf;
	static std::string email;
	static std::string password;
	static std::string userType[2];
	static int type;

	SystemInterface(ocilib::Connection& connection, ocilib::Statement& statement) {
		con = connection;
		st = statement;
	};

	static void SetUserInfo(ocilib::Resultset& rs);
	static bool CheckCommand(int& command, int min, int max);
	static bool is_email_valid(std::string& email);
	static ocilib::Resultset QueryBuilder(std::string str);

	static class Menu {
	public:
		void Starter();
		void Advertiser();
		void Contractor();
		void Profile();
	} Menu;

	static class Loop {
	public:
		void Starter();
		void Advertiser();
		void Contractor();
		void Profile();
	} Loop;

	static class User {
	public:
		void Login();
		void Register();
	} User;

	static class ProfileEditor {
	public:
		void UpdateEmail();
		void UpdateName();
		void UpdatePassword();
	} ProfileEditor;

	static class Component {
	public:
		void Search();
		void Announce();
		void bestSearch();
	} Component;
};

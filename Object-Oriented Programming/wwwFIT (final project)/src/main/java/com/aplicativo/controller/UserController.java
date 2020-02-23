package com.aplicativo.controller;

import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.stereotype.Controller;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

import com.aplicativo.model.User;
import com.aplicativo.service.UserService;

@Controller
public class UserController {

	@Autowired
	private UserService userService;

	@RequestMapping(value = { "/", "/login" }, method = RequestMethod.GET)
	public ModelAndView login() {
		ModelAndView model = new ModelAndView();
		model.setViewName("user/login");
		return model;
	}

	@RequestMapping(value = { "/signup" }, method = RequestMethod.GET)
	public ModelAndView signup() {
		ModelAndView model = new ModelAndView();
		User user = new User();
		model.addObject("user", user);
		model.setViewName("user/signup");
		return model;
	}

	@RequestMapping(value = { "/signup" }, method = RequestMethod.POST)
	public ModelAndView createUser(@Valid User user, BindingResult bindingResult) {
		ModelAndView model = new ModelAndView();
		User userExists = userService.findUserByEmail(user.getEmail());

		if (userExists != null) {
			bindingResult.rejectValue("email", "error.user", "Esse e-mail já está em uso!");
		}
		if (bindingResult.hasErrors()) {
			model.setViewName("user/signup");
		}
		else {
			userService.saveUser(user);
			model.addObject("msg", "Usuario cadastrado com sucesso! Bem-vindo :)");
			model.addObject("user", new User());
			model.setViewName("user/signup");
		}

		return model;
	}

	@RequestMapping(value = { "/about" }, method = RequestMethod.GET)
	public ModelAndView about() {
		ModelAndView model = new ModelAndView();
		model.setViewName("user/about");
		return model;
	}

	@RequestMapping(value = { "/help" }, method = RequestMethod.GET)
	public ModelAndView help() {
		ModelAndView model = new ModelAndView();
		model.setViewName("user/help");
		return model;
	}

	@RequestMapping(value = { "/home/treino1/index" }, method = RequestMethod.GET)
	public ModelAndView treino1() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino1/index");
		return model;
	}

	@RequestMapping(value = { "/home/treino1/curto/1" }, method = RequestMethod.GET)
	public ModelAndView treinoCurto1() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino1/curto/1");
		return model;
	}

	@RequestMapping(value = { "/home/treino1/curto/2" }, method = RequestMethod.GET)
	public ModelAndView treinoCurto2() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino1/curto/2");
		return model;
	}

	@RequestMapping(value = { "/home/treino1/curto/3" }, method = RequestMethod.GET)
	public ModelAndView treinoCurto3() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino1/curto/3");
		return model;
	}

	@RequestMapping(value = { "/home/treino1/curto/4" }, method = RequestMethod.GET)
	public ModelAndView treinoCurto4() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino1/curto/4");
		return model;
	}

	@RequestMapping(value = { "/home/treino1/curto/5" }, method = RequestMethod.GET)
	public ModelAndView treinoCurto5() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino1/curto/5");
		return model;
	}

	@RequestMapping(value = { "/home/treino1/curto/6" }, method = RequestMethod.GET)
	public ModelAndView treinoCurto6() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino1/curto/6");
		return model;
	}

	@RequestMapping(value = { "/home/treino1/longo/1" }, method = RequestMethod.GET)
	public ModelAndView treinoLongo1() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino1/longo/1");
		return model;
	}

	@RequestMapping(value = { "/home/treino1/longo/2" }, method = RequestMethod.GET)
	public ModelAndView treinoLongo2() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino1/longo/2");
		return model;
	}

	@RequestMapping(value = { "/home/treino1/longo/3" }, method = RequestMethod.GET)
	public ModelAndView treinoLongo3() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino1/longo/3");
		return model;
	}

	@RequestMapping(value = { "/home/treino1/longo/4" }, method = RequestMethod.GET)
	public ModelAndView treinoLongo4() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino1/longo/4");
		return model;
	}

	@RequestMapping(value = { "/home/treino1/longo/5" }, method = RequestMethod.GET)
	public ModelAndView treinoLongo5() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino1/longo/5");
		return model;
	}

	@RequestMapping(value = { "/home/treino1/longo/6" }, method = RequestMethod.GET)
	public ModelAndView treinoLongo6() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino1/longo/6");
		return model;
	}

	@RequestMapping(value = { "/home/treino1/longo/7" }, method = RequestMethod.GET)
	public ModelAndView treinoLongo7() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino1/longo/7");
		return model;
	}

	@RequestMapping(value = { "/home/treino1/longo/8" }, method = RequestMethod.GET)
	public ModelAndView treinoLongo8() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino1/longo/8");
		return model;
	}

	@RequestMapping(value = { "/home/treino1/longo/9" }, method = RequestMethod.GET)
	public ModelAndView treinoLongo9() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino1/longo/9");
		return model;
	}

	@RequestMapping(value = { "/home/treino1/longo/10" }, method = RequestMethod.GET)
	public ModelAndView treinoLongo10() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino1/longo/10");
		return model;
	}

	@RequestMapping(value = { "/home/treino1/longo/11" }, method = RequestMethod.GET)
	public ModelAndView treinoLongo11() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino1/longo/11");
		return model;
	}

	@RequestMapping(value = { "/home/treino1/longo/12" }, method = RequestMethod.GET)
	public ModelAndView treinoLongo12() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino1/longo/12");
		return model;
	}

	@RequestMapping(value = { "/home/treino1/longo/13" }, method = RequestMethod.GET)
	public ModelAndView treinoLongo13() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino1/longo/13");
		return model;
	}

	@RequestMapping(value = { "/home/treino1/longo/14" }, method = RequestMethod.GET)
	public ModelAndView treinoLongo14() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino1/longo/14");
		return model;
	}

	@RequestMapping(value = { "/home/treino1/longo/15" }, method = RequestMethod.GET)
	public ModelAndView treinoLongo15() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino1/longo/15");
		return model;
	}

	@RequestMapping(value = { "/home/treino2/index" }, method = RequestMethod.GET)
	public ModelAndView treino2() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino2/index");
		return model;
	}

	@RequestMapping(value = { "/home/treino2/curto/1" }, method = RequestMethod.GET)
	public ModelAndView treino2Curto1() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino2/curto/1");
		return model;
	}

	@RequestMapping(value = { "/home/treino2/curto/2" }, method = RequestMethod.GET)
	public ModelAndView treino2Curto2() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino2/curto/2");
		return model;
	}

	@RequestMapping(value = { "/home/treino2/curto/3" }, method = RequestMethod.GET)
	public ModelAndView treino2Curto3() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino2/curto/3");
		return model;
	}

	@RequestMapping(value = { "/home/treino2/curto/4" }, method = RequestMethod.GET)
	public ModelAndView treino2Curto4() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino2/curto/4");
		return model;
	}

	@RequestMapping(value = { "/home/treino2/medio/1" }, method = RequestMethod.GET)
	public ModelAndView treino2Medio1() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino2/medio/1");
		return model;
	}

	@RequestMapping(value = { "/home/treino2/medio/2" }, method = RequestMethod.GET)
	public ModelAndView treino2Medio2() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino2/medio/2");
		return model;
	}

	@RequestMapping(value = { "/home/treino2/medio/3" }, method = RequestMethod.GET)
	public ModelAndView treino2Medio3() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino2/medio/3");
		return model;
	}

	@RequestMapping(value = { "/home/treino2/medio/4" }, method = RequestMethod.GET)
	public ModelAndView treino2Medio4() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino2/medio/4");
		return model;
	}

	@RequestMapping(value = { "/home/treino2/medio/5" }, method = RequestMethod.GET)
	public ModelAndView treino2Medio5() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino2/medio/5");
		return model;
	}

	@RequestMapping(value = { "/home/treino2/medio/6" }, method = RequestMethod.GET)
	public ModelAndView treino2Medio6() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino2/medio/6");
		return model;
	}

	@RequestMapping(value = { "/home/treino2/medio/7" }, method = RequestMethod.GET)
	public ModelAndView treino2Medio7() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino2/medio/7");
		return model;
	}

	@RequestMapping(value = { "/home/treino2/longo/1" }, method = RequestMethod.GET)
	public ModelAndView treino2Longo1() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino2/longo/1");
		return model;
	}

	@RequestMapping(value = { "/home/treino2/longo/2" }, method = RequestMethod.GET)
	public ModelAndView treino2Longo2() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino2/longo/2");
		return model;
	}

	@RequestMapping(value = { "/home/treino2/longo/3" }, method = RequestMethod.GET)
	public ModelAndView treino2Longo3() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino2/longo/3");
		return model;
	}

	@RequestMapping(value = { "/home/treino2/longo/4" }, method = RequestMethod.GET)
	public ModelAndView treino2Longo4() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino2/longo/4");
		return model;
	}

	@RequestMapping(value = { "/home/treino2/longo/5" }, method = RequestMethod.GET)
	public ModelAndView treino2Longo5() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino2/longo/5");
		return model;
	}

	@RequestMapping(value = { "/home/treino2/longo/6" }, method = RequestMethod.GET)
	public ModelAndView treino2Longo6() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino2/longo/6");
		return model;
	}

	@RequestMapping(value = { "/home/treino2/longo/7" }, method = RequestMethod.GET)
	public ModelAndView treino2Longo7() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino2/longo/7");
		return model;
	}

	@RequestMapping(value = { "/home/treino2/longo/8" }, method = RequestMethod.GET)
	public ModelAndView treino2Longo8() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino2/longo/8");
		return model;
	}

	@RequestMapping(value = { "/home/treino2/longo/9" }, method = RequestMethod.GET)
	public ModelAndView treino2Longo9() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino2/longo/9");
		return model;
	}

	@RequestMapping(value = { "/home/treino2/longo/10" }, method = RequestMethod.GET)
	public ModelAndView treino2Longo10() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino2/longo/10");
		return model;
	}

	@RequestMapping(value = { "/home/treino3/index" }, method = RequestMethod.GET)
	public ModelAndView treino3() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino3/index");
		return model;
	}

	@RequestMapping(value = { "/home/treino3/1/index" }, method = RequestMethod.GET)
	public ModelAndView treino3_1_index() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino3/1/index");
		return model;
	}

	@RequestMapping(value = { "/home/treino3/1/curto/1" }, method = RequestMethod.GET)
	public ModelAndView treino3_1_curto1() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino3/1/curto/1");
		return model;
	}

	@RequestMapping(value = { "/home/treino3/1/curto/2" }, method = RequestMethod.GET)
	public ModelAndView treino3_1_curto2() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino3/1/curto/2");
		return model;
	}

	@RequestMapping(value = { "/home/treino3/1/curto/3" }, method = RequestMethod.GET)
	public ModelAndView treino3_1_curto3() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino3/1/curto/3");
		return model;
	}

	@RequestMapping(value = { "/home/treino3/1/curto/4" }, method = RequestMethod.GET)
	public ModelAndView treino3_1_curto4() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino3/1/curto/4");
		return model;
	}

	@RequestMapping(value = { "/home/treino3/1/medio/1" }, method = RequestMethod.GET)
	public ModelAndView treino3_1_medio1() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino3/1/medio/1");
		return model;
	}

	@RequestMapping(value = { "/home/treino3/1/medio/2" }, method = RequestMethod.GET)
	public ModelAndView treino3_1_medio2() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino3/1/medio/2");
		return model;
	}

	@RequestMapping(value = { "/home/treino3/1/medio/3" }, method = RequestMethod.GET)
	public ModelAndView treino3_1_medio3() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino3/1/medio/3");
		return model;
	}

	@RequestMapping(value = { "/home/treino3/1/medio/4" }, method = RequestMethod.GET)
	public ModelAndView treino3_1_medio4() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino3/1/medio/4");
		return model;
	}

	@RequestMapping(value = { "/home/treino3/1/medio/5" }, method = RequestMethod.GET)
	public ModelAndView treino3_1_medio5() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino3/1/medio/5");
		return model;
	}

	@RequestMapping(value = { "/home/treino3/1/medio/6" }, method = RequestMethod.GET)
	public ModelAndView treino3_1_medio6() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino3/1/medio/6");
		return model;
	}

	@RequestMapping(value = { "/home/treino3/1/medio/7" }, method = RequestMethod.GET)
	public ModelAndView treino3_1_medio7() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino3/1/medio/7");
		return model;
	}

	@RequestMapping(value = { "/home/treino3/1/longo/1" }, method = RequestMethod.GET)
	public ModelAndView treino3_1_longo1() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino3/1/longo/1");
		return model;
	}

	@RequestMapping(value = { "/home/treino3/1/longo/2" }, method = RequestMethod.GET)
	public ModelAndView treino3_1_longo2() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino3/1/longo/2");
		return model;
	}

	@RequestMapping(value = { "/home/treino3/1/longo/3" }, method = RequestMethod.GET)
	public ModelAndView treino3_1_longo3() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino3/1/longo/3");
		return model;
	}

	@RequestMapping(value = { "/home/treino3/1/longo/4" }, method = RequestMethod.GET)
	public ModelAndView treino3_1_longo4() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino3/1/longo/4");
		return model;
	}

	@RequestMapping(value = { "/home/treino3/1/longo/5" }, method = RequestMethod.GET)
	public ModelAndView treino3_1_longo5() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino3/1/longo/5");
		return model;
	}

	@RequestMapping(value = { "/home/treino3/1/longo/6" }, method = RequestMethod.GET)
	public ModelAndView treino3_1_longo6() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino3/1/longo/6");
		return model;
	}

	@RequestMapping(value = { "/home/treino3/1/longo/7" }, method = RequestMethod.GET)
	public ModelAndView treino3_1_longo7() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino3/1/longo/7");
		return model;
	}

	@RequestMapping(value = { "/home/treino3/1/longo/8" }, method = RequestMethod.GET)
	public ModelAndView treino3_1_longo8() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino3/1/longo/8");
		return model;
	}

	@RequestMapping(value = { "/home/treino3/1/longo/9" }, method = RequestMethod.GET)
	public ModelAndView treino3_1_longo9() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino3/1/longo/9");
		return model;
	}

	@RequestMapping(value = { "/home/treino3/1/longo/10" }, method = RequestMethod.GET)
	public ModelAndView treino3_1_longo10() {
		ModelAndView model = new ModelAndView();
		model.setViewName("/home/treino3/1/longo/10");
		return model;
	}

	@RequestMapping(value = { "home/about" }, method = RequestMethod.GET)
	public ModelAndView homeAbout() {

		ModelAndView model = new ModelAndView();
		Integer exercises = 0;
		Authentication auth = SecurityContextHolder.getContext().getAuthentication();
		User user = userService.findUserByEmail(auth.getName());

		// se o usuario fez o treino de alongamento
		if (user.getFezExercicio1() == 1)
			exercises += 20;

		// se o usuario fez o treino de cardio
		if (user.getFezExercicio2() == 1)
			exercises += 30;

		// se o usuario fez o treino de forca
		if (user.getFezExercicio3() == 1)
			exercises += 50;

		// criando objeto $fullName com o nome completo do usuario
		model.addObject("fullName", user.getFirstname() + " " + user.getLastname());

		// criando objeto $firstName com o primeiro nome do usuario
		model.addObject("firstName", user.getFirstname());

		// criando objeto $progress com o progresso (treinos concluidos) do usuario
		model.addObject("progress", exercises);

		model.setViewName("home/about");
		return model;
	}

	@RequestMapping(value = { "home/help" }, method = RequestMethod.GET)
	public ModelAndView homeHelp() {

		Integer exercises = 0;
		ModelAndView model = new ModelAndView();
		Authentication auth = SecurityContextHolder.getContext().getAuthentication();
		User user = userService.findUserByEmail(auth.getName());

		// se o usuario fez o treino de alongamento
		if (user.getFezExercicio1() == 1)
			exercises += 20;

		// se o usuario fez o treino de cardio
		if (user.getFezExercicio2() == 1)
			exercises += 30;

		// se o usuario fez o treino de forca
		if (user.getFezExercicio3() == 1)
			exercises += 50;

		// criando objeto $fullName com o nome completo do usuario
		model.addObject("fullName", user.getFirstname() + " " + user.getLastname());

		// criando objeto $firstName com o primeiro nome do usuario
		model.addObject("firstName", user.getFirstname());

		// criando objeto $progress com o progresso (treinos concluidos) do usuario
		model.addObject("progress", exercises);

		model.setViewName("home/help");
		return model;
	}

	@RequestMapping(value = { "/home/home" }, method = RequestMethod.GET)
	public ModelAndView home() {

		ModelAndView model = new ModelAndView();
		Authentication auth = SecurityContextHolder.getContext().getAuthentication();
		User user = userService.findUserByEmail(auth.getName());
		Integer exercises = 0, didFirstTrainning = 0, didSecondTrainning = 0, didThirdTrainning = 0;
		String msg1 = null, msg2 = null, msg3 = null;

		// se o usuario fez o treino de alongamento
		if (user.getFezExercicio1() == 1) {
			exercises += 20;
			didFirstTrainning = 1;
			msg1 = "Você já fez o treino de alongamento";

		}

		// se o usuario fez o treino de cardio
		if (user.getFezExercicio2() == 1) {
			exercises += 30;
			didSecondTrainning = 1;
			msg2 = "Você já fez o treino de cardio";
		}

		// se o usuario fez o treino de forca
		if (user.getFezExercicio3() == 1) {
			exercises += 50;
			didThirdTrainning = 1;
			msg3 = "Você já fez o treino de força";
		}

		// criando objeto $fullName com o nome completo do usuario
		model.addObject("fullName", user.getFirstname() + " " + user.getLastname());

		// criando objeto $firstName com o primeiro nome do usuario
		model.addObject("firstName", user.getFirstname());

		// criando objeto $progress com o progresso (treinos concluidos) do usuario
		model.addObject("progress", exercises);

		// criando objeto $didFirstT que avisa se ousuario fez o primeiro treino
		model.addObject("didFirstT", didFirstTrainning);

		// criando objeto $didSecondT que avisa se ousuario fez o primeiro treino
		model.addObject("didSecondT", didSecondTrainning);

		// criando objeto $didThirdT que avisa se ousuario fez o primeiro treino
		model.addObject("didThirdT", didThirdTrainning);

		// criando objeto usuario
		model.addObject("user", user);
		
		model.addObject("doneEx1", msg1);
		model.addObject("doneEx2", msg2);
		model.addObject("doneEx3", msg3);

		// redirecionando o usuario para a sua home
		model.setViewName("home/home");

		return model;
	}

	@RequestMapping(value = { "/access_denied" }, method = RequestMethod.GET)
	public ModelAndView accessDenied() {
		ModelAndView model = new ModelAndView();
		model.setViewName("errors/access_denied");
		return model;
	}

	@RequestMapping(value = { "/addExercise1" }, method = RequestMethod.GET)
	public ModelAndView addExercise1() {
		Authentication auth = SecurityContextHolder.getContext().getAuthentication();
		User user = userService.findUserByEmail(auth.getName());
		userService.addExercise1(user);
		return home();
	}

	@RequestMapping(value = { "/addExercise2" }, method = RequestMethod.GET)
	public ModelAndView addExercise2() {
		Authentication auth = SecurityContextHolder.getContext().getAuthentication();
		User user = userService.findUserByEmail(auth.getName());
		userService.addExercise2(user);
		return home();
	}

	@RequestMapping(value = { "/addExercise3" }, method = RequestMethod.GET)
	public ModelAndView addExercise3() {
		Authentication auth = SecurityContextHolder.getContext().getAuthentication();
		User user = userService.findUserByEmail(auth.getName());
		userService.addExercise3(user);
		return home();
	}

	@RequestMapping(value = { "/changeFirstname" }, method = RequestMethod.GET)
	public ModelAndView changeFirstname(String firstname) {
		ModelAndView model = home();

		Authentication auth = SecurityContextHolder.getContext().getAuthentication();
		User user = userService.findUserByEmail(auth.getName());
		userService.changeFirstname(user, firstname);

		model.addObject("msg", "Primeiro nome alterado com sucesso para " + firstname);

		return model;

	}

	@RequestMapping(value = { "/changeSecondname" }, method = RequestMethod.GET)
	public ModelAndView changeSecondname(String secondname) {
		ModelAndView model = home();

		Authentication auth = SecurityContextHolder.getContext().getAuthentication();
		User user = userService.findUserByEmail(auth.getName());
		userService.changeFirstname(user, secondname);

		model.addObject("msg", "Segundo nome alterado com sucesso para " + secondname);

		return model;

	}
}

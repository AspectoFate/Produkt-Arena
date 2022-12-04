import 'package:flutter/material.dart';
import 'package:flutter_app/models/user.dart';
import 'package:flutter_app/screens/authenticate/authenticate.dart';
import 'package:flutter_app/screens/home/home.dart';
import 'package:flutter_app/services/auth.dart';

class Wrapper extends StatelessWidget {
  const Wrapper({super.key});

  @override
  Widget build(BuildContext context) {
    //return either home or auth widget

    return const Authenticate();
  }
}

import 'package:flutter/material.dart';
import 'package:sih/statess.dart';

class Drop extends StatefulWidget {
  @override
  _DropState createState() => _DropState();
}

class _DropState extends State<Drop> {
  OurState stateName;
  @override
  Widget build(BuildContext context) {
    return DropdownButton(
      hint: new Text("Select gender"),
      isDense: true,
      value: stateName == null ? null : stateName,
      onChanged: (OurState newValue) {
        setState(() {
          stateName = newValue;
          print(stateName.name);
        });
      },
      items: OurState.ourstateList().map<DropdownMenuItem<OurState>>((user) {
        return new DropdownMenuItem(
          value: user,
          child: stateName == null
              ? new Text(
                  user.name,
                  style: new TextStyle(color: Colors.grey),
                )
              : stateName.name == user.name
                  ? new Text(
                      user.name,
                      style: new TextStyle(color: Colors.black),
                    )
                  : new Text(
                      user.name,
                      style: new TextStyle(color: Colors.grey),
                    ),
        );
      }).toList(),
    );
  }
}

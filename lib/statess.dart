class OurState {
  final int id;
  final String name;

  OurState(
    this.id,
    this.name,
  );

  static List<OurState> ourstateList() {
    return <OurState>[
      OurState(
        1,
        'Gujarat',
      ),
      OurState(
        2,
        'Maharashtra',
      )
    ];
  }
}
